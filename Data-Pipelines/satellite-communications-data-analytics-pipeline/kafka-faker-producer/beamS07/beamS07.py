import random
from faker.providers import BaseProvider
import datetime
import time


class BeamS07(BaseProvider):
    def remoteId(self):
        remoteIds=["B3010","B3256","C1710","C4432","C5510"]
        return random.choice(remoteIds)

    def fwdModCodId(self):
        data= [10, 11, 12, 13]
        weights=[0.7,0.1,0.1,0.1]
        return random.choices(data,weights)

    def fwdSNR(self):
        minimum=4
        maximum=7


        return round(random.uniform(minimum,maximum),1)

    def packetsLost(self):
        minimum=100
        maximum=500

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
                "beamId":136,
                "beamName":"BeamS07",
                "satLong":-129.2,
                "fwdModCodId":FakerInstance.fwdModCodId(),
                "fwdSNR":FakerInstance.fwdSNR(),
                "packetsLost":FakerInstance.packetsLost(),
                "latitude":60.4,
                "longitude":-113.8,
                "rxFreq":12200150,
                "txFreq":14700580,
                "fwdBitRate":14.0
                }
        key={"beamName":"BeamS07"}
        return message,key
        

