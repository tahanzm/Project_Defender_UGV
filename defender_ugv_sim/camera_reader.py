import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from rclpy.qos import qos_profile_sensor_data # <-- Bu ayar çalışıyor, bunu kullanacağız!
from ultralytics import YOLO

class CameraReader(Node):
    def __init__(self):
        super().__init__('camera_reader_node')
        
        self.bridge = CvBridge()
        
        # 1. YOLO Modelini Yükle
        self.get_logger().info('YOLO Modeli Yukleniyor... (Biraz sürebilir)')
        self.model = YOLO("yolov8n.pt") 
        self.get_logger().info('YOLO Modeli Hazir! 🚀')
        
        # 2. Kameraya Abone Ol
        # Önceki hatanda burası çalışıyordu, o yüzden bu ayara güveniyoruz.
        self.subscription = self.create_subscription(
            Image,
            '/my_camera_sensor/image_raw', # <-- Doğru Topic
            self.listener_callback,
            qos_profile=qos_profile_sensor_data) # <-- Doğru Ayar

        self.get_logger().info('KAMERA BAGLANTISI KURULDU! Görüntü Bekleniyor...')

    def listener_callback(self, msg):
        try:
            # Görüntüyü çevir
            current_frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            
            # --- YAPAY ZEKA KISMI ---
            # Hassasiyet: %1 (conf=0.01) - Her şeyi görsün
            results = self.model(current_frame, conf=0.50) 

            # Terminale çalıştığını göstermek için nokta bas
            print(".", end="", flush=True)

            if len(results[0].boxes) > 0:
                 print(f"\nBULDUM! Nesne Sayısı: {len(results[0].boxes)}")

            # Kutucuklu Görüntüyü Çiz
            annotated_frame = results[0].plot()

            # Ekrana Yazdır
            cv2.imshow("Defender Bot - AI Vision", annotated_frame)
            cv2.waitKey(1)
            
        except Exception as e:
            self.get_logger().error(f'Hata: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = CameraReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()