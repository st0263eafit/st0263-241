
from concurrent import futures

import grpc
import Service_pb2
import Service_pb2_grpc

HOST = '[::]:8080'

class ProductService(Service_pb2_grpc.ProductServiceServicer):
   
   def AddProduct(self, request, context):
      print("Request is received: " + str(request))
      return Service_pb2.TransactionResponse(status_code=1)
 
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Service_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
  server.add_insecure_port(HOST)
  print("Service is running... ")
  server.start()
  server.wait_for_termination()

if __name__ == "__main__":
    serve()