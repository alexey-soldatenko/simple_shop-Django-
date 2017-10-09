from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'my_shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^delete_product/(?P<product_id>\d+)$', 'cart.views.delete_product_in_cart'),

     url(r'^my_cart/?(?P<page>\d+)?$', 'cart.views.display_cart'),

     url(r'^search/$', 'search.views.display_search'),

    url(r'^catalog/(?P<page>\d+)?$', 'catalog.views.display_catalog'),

    url(r'^(?P<manufacturer>\w+)/(?P<product_slug>\w+)$', 'catalog.views.display_product_page'),

    url(r'^add_to_cart$', 'cart.views.add_to_cart'),

    url(r'^$', 'catalog.views.display_home'), 

    url(r'^catalog/', include('catalog.urls')),

    url(r'^my_order$', 'order.views.display_order'),

    url(r'^save_order$', 'order.views.save_order'),

    url(r'^our_shops$', 'catalog.views.display_our_shops', {'param': 'shops'}),
    url(r'^payments_and_delivery$', 'catalog.views.display_our_shops', {'param': 'delivery'}),
    url(r'^warranty$', 'catalog.views.display_our_shops', {'param': 'warranty'}),

    url(r'^contacts$', 'catalog.views.display_our_shops', {'param': 'contacts'}),

    url(r'^about_us$', 'catalog.views.display_our_shops', {'param': 'about_us'}),

    url(r'^login$', 'auth_shop.views.display_auth', {'param':'login'}), 

    url(r'^log_in$', 'auth_shop.views.user_login'), 

    url(r'^sign_up$', 'auth_shop.views.display_auth', {'param':'sign_up'}), 
    
    url(r'^save$', 'auth_shop.views.save'),

    url(r'^my_account', 'auth_shop.views.display_account'),

    url(r'^logout$', 'auth_shop.views.user_logout'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'auth_shop.views.activate_account', name='activate'),
  
]

handler404 = 'catalog.views.display_404'
