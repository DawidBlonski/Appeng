from rest_framework import routers
from appeng import api_views as appengs_api_views 

router = routers.DefaultRouter()

router.register(r'Words',appengs_api_views.WordsViewset)
router.register(r'User_answer',appengs_api_views.User_answerViewset)