import random
from faker.providers import BaseProvider
import datetime
import time


class BeamS11(BaseProvider):
    def remoteId(self):
        remoteIds=["B3010","B3256","C1710","C4432","C5510"]
        return random.choice(remoteIds)

    def fwdModCodId(self):
        data= [8,9,10,11]
        weights=[0.7,0.1,0.1,0.1]
        return random.choices(data,weights)

    def fwdSNR(self):
        minimum=6
        maximum=10


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
                "beamId":124,
                "beamName":"BeamS11",
                "satLong":-129.2,
                "fwdModCodId":FakerInstance.fwdModCodId(),
                "fwdSNR":FakerInstance.fwdSNR(),
                "packetsLost":FakerInstance.packetsLost(),
                "latitude":50.5,
                "longitude":-112.8,
                "rxFreq":12800950,
                "txFreq":14000525,
                "fwdBitRate":17.0
                }
        key={"beamName":"BeamS07"}
        return message,key
        

