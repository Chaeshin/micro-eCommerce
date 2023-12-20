from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from Order.models import OrderItem
from Product.models import Product
from Review.models import Review


class toReview(View):
    template = 'ReviewsPage_ToReview.html'

    def get(self, request):
        customer_id = request.user.user_id  #Kuha currently logged in customer
        images = OrderItem.objects.filter(customer_id=customer_id, status=0)
        with connection.cursor() as cursor:
            cursor.callproc('get_orders_to_review', [customer_id])#Kuha mga need e review
            orders_result = cursor.fetchall()

        orders_and_images = zip(orders_result, images)
        orders = []#I sud og array mga need e review para ma display sa html
        for (order_result, image) in orders_and_images:
            order_item_id, product_id, customer_id, quantity, price, product_name, picture = order_result
            order_image = image.product.picture
            orders.append({
                'order_item_id': order_item_id,
                'product_id': product_id,
                'customer_id': customer_id,
                'quantity': quantity,
                'price': price,
                'product_name': product_name,
                'picture': order_image,
            })

        return render(request, self.template, {'orders': orders})


class myReview(View):
    template = 'ReviewsPage_MyReviews.html'

    def get(self, request):
        customer_id = request.user.user_id #Kuha currently logged in customer
        rev_pro_img = Review.objects.filter(orderitem_id_id__customer_id=customer_id)

        with connection.cursor() as cursor:
            cursor.callproc('get_customer_reviews', [customer_id])#Kuha mga manag review
            reviews_result = cursor.fetchall()

        reviews_and_images = zip(reviews_result, rev_pro_img)
        reviews = []#I sud og array mga manag review para ma display sa html
        for (review_result, review) in reviews_and_images:
            review_id, comment, rate, date, time, product_id, product_name, picture = review_result
            product = review.orderitem_id.product.picture

            reviews.append({
                'review_id': review_id,
                'comment': comment,
                'rate': rate,
                'date': date,
                'time': time,
                'product_id': product_id,
                'product_name': product_name,
                'images': product,
            })

        return render(request, self.template, {'reviews': reviews})


class productReview(View):
    template = 'ReviewsPage.html'

    def get(self, request, orderitem_id):
        order_item = OrderItem.objects.get(order_item_id=orderitem_id)
        product_image = order_item.product.picture
        print(product_image)
        with connection.cursor() as cursor:
            cursor.callproc('get_product_details', [order_item.product_id])
            product_details = cursor.fetchall()
            cursor.nextset()

            cursor.callproc('get_orderitem_details', [order_item])
            orderitem_details = cursor.fetchall()

        if product_details and orderitem_details:
            product_result = product_details[0]
            name, price, description, image = product_result
            orderitem_result = orderitem_details[0]
            quantity, price = orderitem_result

        else:
            name, price, description, image = '', 0, '', ''
            quantity, price = 0, 0
        context = {
            'product_name': name,
            'product_price': price,
            'product_description': description,
            'product_image': product_image,
            'order_quantity': quantity,
            'order_price': price
        }
        return render(request, self.template, context)

    def post(self, request, orderitem_id):
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')

        # Call the stored procedure to add the review and update status
        with connection.cursor() as cursor:
            cursor.callproc('add_product_review', [orderitem_id, comment, rating])

        return redirect('Review:toReview')


class ViewProduct(View):
    template = 'ViewProduct.html'

    def get(self, request, product_id):
        # reviews = Review.objects.filter(orderitem_id__product_id=product_id)
        product = Product.objects.get(pk=product_id)
        product_image = product.picture
        with connection.cursor() as cursor:
            cursor.callproc('get_product_details', [product_id])#Kuha product details kung picture iyang gi pislit
            product_details_result = cursor.fetchall()
            cursor.nextset()

            cursor.callproc('get_product_totalsales_and_averagerating', [product_id])#Kuha total sales og average rating sa product
            sales_rating = cursor.fetchall()
            cursor.nextset()

            cursor.callproc('get_product_reviews', [product_id])#Kuha mga reviews sa product
            reviews_result = cursor.fetchall()

        if product_details_result and sales_rating:
            product_result = product_details_result[0]
            name, price, description,image = product_result
            product_rs_result = sales_rating[0]
            total_sale, average_rating = product_rs_result
            print(image)
        else:
            name, price, description,image = '', 0,'', ''
            total_sale, average_rating = 0, 0

        review = []
        for review_result in reviews_result:#para sa mga review sa product
            id, comment, rate, date, time = review_result
            review.append({
                'review_id': id,
                'review_comment': comment,
                'review_rate': rate,
                'review_date': date,
                'review_time': time,
            })

        context = {
            'product_name': name,
            'product_price': price,
            'product_description': description,
            'review_product': product_image,
            'product_total_sale': total_sale,
            'product_average_rating': average_rating,
            'reviews': review
        }
        return render(request, self.template, context)

