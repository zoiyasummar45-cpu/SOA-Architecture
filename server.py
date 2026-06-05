import grpc
from concurrent import futures
import weather_pb2
import weather_pb2_grpc

class WeatherService(weather_pb2_grpc.WeatherServiceServicer):
    def GetWeatherStats(self, request, context):
        temps = request.temperatures
        avg_temp = sum(temps) / len(temps)
        min_temp = min(temps)
        max_temp = max(temps)
        
        return weather_pb2.WeatherResponse(
            average=avg_temp,
            min=min_temp,
            max=max_temp
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()