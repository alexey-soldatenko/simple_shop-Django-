from django.conf.urls import url 

urlpatterns = [
	url(r'^(?P<manufacturer>manufacturer_\w+/)?(?P<kind>kinds_\w+/)?(?P<price>price_\d+-\d+/)?(?P<diagonal>diagonal_\w+/)?(?P<display>display_\w+/)?(?P<processor>processor_\w+/)?(?P<ram>ram_\w+/)?(?P<grafic>grafic_\w+/)?(?P<hdd>hdd_\d+-\d+/)?(?P<dvd>dvd_\w+/)?(?P<os>os_\w+/)?(?P<webcam>webcam_[a-zA-z0-9.]*/)?(?P<weight>weight_\w\.?\w?-\w\.?\w?/)?(?P<page>\d+)?$', 'catalog.views.products_filter'),

]