
from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.HiHoStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="geralt"))
        print("Greeter client received(SayHello): " + response.message)
        response = stub.SayBye(helloworld_pb2.ByeRequest(name="nobody"))
        print("Greeter client received(SayBye): " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
