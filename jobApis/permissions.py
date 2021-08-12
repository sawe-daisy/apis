from rest_framework import permissions

# class employerPost(permissions.BasePermission):
def can_post_job(self, request, view, obj):
    if self.user.user_type == "EM":
        return True
    else:
        False