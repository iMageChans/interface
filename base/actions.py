from utils import keystone
from utils.JSONExtractor import JSONExtractor


class BaseAction:
    def __init__(self, validated_data):
        self.keypair = keystone.check_keypair(keypair=validated_data['keypair'], path=validated_data['path'])
        try:
            self.account_id = keystone.ValidAddress(
                validated_data.get('account_id', f"Dn{self.keypair.ss58_address}")
            )
        except Exception as e:
            print("error:", e)

        self.results = None

    def result(self):
        pass

    def is_success(self):
        pass


class BaseActionsRead(BaseAction):
    def __init__(self, validated_data):
        super().__init__(validated_data)

    def serializers(self):
        values = JSONExtractor().get_data_or_err(self.results.value_serialized)
        return values

    def is_success(self):
        if JSONExtractor().get_data_or_err(self.results.value_serialized):
            return True
        return False


class BaseActionsExec(BaseAction):
    def __init__(self, validated_data):
        super().__init__(validated_data)

    def serializers(self):
        values = JSONExtractor().get_transfer_data(self.results)
        return values

    def is_success(self):
        return self.results.is_success
