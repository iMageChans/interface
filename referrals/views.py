from base.views import BaseView
from referrals import serializers
from referrals import actions


class GetDirectReferralsCountView(BaseView):
    serializer_class = serializers.GetDirectReferralsCountSerializer
    action_class = actions.GetDirectReferralsCount

