import random
from faker.providers import BaseProvider
import datetime
import time


class BeamS17(BaseProvider):
    def remoteId(self):
        remoteIds=["B3010","B3256","C1710","C4432","C5510"]
        return random.choice(remoteIds)

    def fwdModCodId(self):
        data= [10,11,12,13]
        weights=[0.7,0.1,0.1,0.1]
        return random.choices(data,weights)

    def fwdSNR(self):
        minimum=8
        maximum=12
        return round(random.uniform(minimum,maximum),1)

    def packetsLost(self):
        minimum=0
        maximum=10

        return random.randint(minimum,maximum)

    def produce_msg(
            self,
            FakerInstance,
            count=1
            ):
        
        message={
                "datetime": datetime.datetime.fromtimestamp(time.time()).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
                "remoteId":FakerInstance.remoteId(),
                "beamId":107,
                "beamName":"BeamS17",
                "satLong":-129.2,
                "fwdModCodId":FakerInstance.fwdModCodId(),
                "fwdSNR":FakerInstance.fwdSNR(),
                "packetsLost":FakerInstance.packetsLost(),
                "latitude":40.7,
                "longitude":-111.9,
                "rxFreq":12500750,
                "txFreq":14010500,
                "fwdBitRate":20.0
                }
        key={"beamName":"BeamS17"}
        return message,key
        

