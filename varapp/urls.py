from django.urls import path
from varapp.views.main_views import *
from varapp.views.accounts_views import *
from varapp.views.bookmarks_views import *
from varapp.views.auth_views import *

urlpatterns = [
    path('', index),

    # users_db
    path('authenticate', authenticate),
    path('renew_token', renew_token),
    path('signup', signup),
    path('resetPasswordRequest', reset_password_request),
    path('changePassword', change_password),
    path('deleteUser', p_delete_user),
    path('userActivation', p_user_activation),
    path('attributeDb', p_attribute_db),
    path('changeAttribute', p_change_attribute),
    path('usersInfo', p_get_users_info),
    path('dbsInfo', p_get_dbs_info),
    path('rolesInfo', p_get_roles_info),

    # variants_db
    path('<db>/count', count, name='count'),
    path('<db>/samples', p_samples, name='samples'),
    path('<db>/variants', p_variants, name='variants'),
    path('<db>/variants/export', p_export_variants, name='export'),
    path('<db>/stats', p_stats, name='stats'),
    path('<db>/location/autocomplete/(?P<prefix>[\w\-,:\s]+)', location_names_autocomplete),
    path('<db>/location/(?P<loc>[\w\-,:\s]+)', location_find),
    path('<db>/getBookmarks', p_get_bookmarks),
    path('<db>/setBookmark', p_set_bookmark),
    path('<db>/deleteBookmark', p_delete_bookmark),

    # Older shorter versions with the default db
    path('location/autocomplete/(?P<prefix>[\w\-,:\s]+)', location_names_autocomplete),
    path('location/(?P<loc>[\w\-,:\s]+)', location_find),
]

