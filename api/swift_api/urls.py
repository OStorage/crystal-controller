from django.conf.urls import url
from . import views

urlpatterns = [
    # Storages Policies
    url(r'^storage_policies/?$', views.storage_policies),
    url(r'^storage_policies/deployed?$', views.deployed_storage_policies),
    url(r'^storage_policies/load?$', views.load_swift_policies),
    url(r'^storage_policy/(?P<storage_policy_id>[^/]+)/?$', views.storage_policy_detail),
    url(r'^storage_policy/(?P<storage_policy_id>[^/]+)/disk/?$', views.storage_policy_disks),
    url(r'^storage_policy/(?P<storage_policy_id>[^/]+)/disk/(?P<disk_id>[^/]+)/?$', views.delete_storage_policy_disks),
    url(r'^storage_policy/(?P<storage_policy_id>[^/]+)/deploy/?$', views.deploy_storage_policy),

    # Object Placement
    url(r'^locality/(?P<account>\w+)(?:/(?P<container>[-\w]+))(?:/(?P<swift_object>[-\w]+))?/$', views.locality_list),

    # url(r'^sort_nodes/?$', views.sort_list),
    # url(r'^sort_nodes/(?P<sort_id>[0-9]+)/?$', views.sort_detail),

    # Nodes
    url(r'^nodes/?$', views.node_list),
    url(r'^nodes/(?P<server_type>[^/]+)/(?P<node_id>[^/]+)/?$', views.node_detail),
    url(r'^nodes/(?P<server_type>[^/]+)/(?P<node_id>[^/]+)/restart/?$', views.node_restart),

    # Regions
    url(r'^regions/?$', views.regions),
    url(r'^regions/(?P<region_id>[^/]+)/?$', views.region_detail),
    url(r'^zones/?$', views.zones),
    url(r'^zones/(?P<zone_id>[^/]+)/?$', views.zone_detail),

    # Containers
    url(r'^(?P<project_id>[^/]+)/containers/?$', views.containers_list),
    url(r'^(?P<project_id>[^/]+)/(?P<container_name>[^/]+)/create?$', views.create_container),
    url(r'^(?P<project_id>[^/]+)/(?P<container_name>[^/]+)/policy?$', views.update_container),

]
