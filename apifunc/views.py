from django.http import JsonResponse
from django.core.cache import cache
from .models import Product
from django.core.serializers import serialize

# 전체 조회
def product_list(request):
    cache_key = 'full_product_list'  # 캐시에 데이터를 저장할 때 사용할 키를 지정
    cached_data = cache.get(cache_key)  # 캐시에서 데이터를 가져와서 cached_data에 저장
    if cached_data:  # 캐시된 데이터가 있다면
        return JsonResponse(cached_data, safe=False)  # 해당 데이터를 JSON 형식으로 응답으로 반환
    products = list(Product.objects.all().values('id', 'name', 'price', 'is_featured'))
    cache.set(cache_key, products, timeout=3600)  # 가져온 제품 목록을 캐시에 저장, 캐시의 유효 기간은 3600초(1시간)으로 설정
    return JsonResponse(products, safe=False)  # 새로 가져온 제품 목록을 JSON 형식으로 응답으로 반환

# 추천상품 조회
def featured_products(request):
    cache_key = 'featured_product_list'
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)
    products = list(Product.objects.filter(is_featured=True).values('id', 'name', 'price'))  # is_featured : 추천 상품 필터링
    cache.set(cache_key, products, timeout=3600)
    return JsonResponse(products, safe=False)