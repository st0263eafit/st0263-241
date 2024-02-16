import dotenv from 'dotenv';
import grpc from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

dotenv.config()

const PROTO_PATH = process.env.PROTO_PATH;
const REMOTE_HOST = process.env.REMOTE_HOST;

const packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });

console.info("Consumer service is started...");

const productService = grpc.loadPackageDefinition(packageDefinition).ProductService;

function main(){

  const idProduct = 1;
  const client = new productService(REMOTE_HOST,grpc.credentials.createInsecure());

  client.AddProduct({id_product: idProduct} , (err, data) => {

    if(err){
      console.log(err);
    } else {
      console.log('Response received from remote service:', data); // API response
    }
   });

};

main();