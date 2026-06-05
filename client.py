import grpc
import weather_pb2
import weather_pb2_grpc

def run():
    # Establish connection with the server
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = weather_pb2_grpc.WeatherServiceStub(channel)
        
        # Defining a list of 5 weather temperatures
        temps_list = [25.5, 30.2, 28.1, 22.4, 27.8]
        
        # Sending the request to the server
        response = stub.GetWeatherStats(weather_pb2.WeatherRequest(temperatures=temps_list))
        
        # Printing the results received from the server
        print(f"Results from the server:")
        print(f"Average: {response.average:.2f}")
        print(f"Minimum: {response.min}")
        print(f"Maximum: {response.max}")

if __name__ == '__main__':
    run()