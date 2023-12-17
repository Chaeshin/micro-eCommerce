from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from Order.models import OrderItem
from Review.models import Review


class toReview(View):
    template = 'ReviewsPage_ToReview.html'

    def get(self,request):
        orders = OrderItem.objects.filter(status=0,customer_id=request.user.customer)
        print(request.user.customer)
        return render(request, self.template,{'orders': orders})


class myReview(View):
    template = 'ReviewsPage_MyReviews.html'

    def get(self,request):
        reviews = Review.objects.filter(customer_id=request.user.customer)
        return render(request, self.template,{'reviews': reviews})


class productReview(View):
    template = 'ReviewsPage.html'

    def get(self, request, orderitem_id):
        # Retrieve the product details based on the product ID
        product = OrderItem.objects.get(order_item_id=orderitem_id)
        return render(request, self.template, {'order_item': product})

    def post(self, request, orderitem_id):
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        print(orderitem_id)
        print(comment)
        print(rating)
        order_item = OrderItem.objects.get(order_item_id=orderitem_id)
        customer = request.user.customer
        # Validate and save to the database using your Review model
        review = Review.objects.create(
            customer=customer,
            orderitem_id=order_item,
            comment=comment,
            rate=rating
        )
        review.save()

        order_item.status = 1
        order_item.save()
        return redirect('Review:toReview')