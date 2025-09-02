import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # 根据实际消息类型修改
from model.NavGPT_model import NavGPTv2_Inference 
class NavGPTv2Subscriber(Node):
    """
    NavGPTv2话题订阅节点类
    用于订阅NavGPTv2话题并处理接收到的消息
    """
    
    def __init__(self):
        """
        初始化节点、订阅者和相关变量
        """
        super().__init__('navgptv2_subscriber')  # 初始化节点，名称为'navgptv2_subscriber'
        
        # 创建订阅者，订阅名为"NavGPTv2"的话题
        # 使用String消息类型，队列大小为10
        # 可根据实际需要更换消息类型
        self.subscription = self.create_subscription(
            String,  # 消息类型，可根据需要修改
            'NavGPTv2',  # 话题名称
            self.listener_callback,  # 回调函数
            10  # 队列大小
        )
        
        # 防止未使用变量警告
        self.subscription  
        
        self.get_logger().info('NavGPTv2 订阅节点已启动，等待消息...')
    
    def listener_callback(self, msg):
        """
        话题消息回调函数
        当接收到新消息时自动调用此函数
        
        Args:
            msg: 接收到的消息对象
        """
        self.get_logger().info(f'收到消息: "{msg.data}"')
        
        # 调用NavGPTv2推理函数处理接收到的消息
        try:
            result = NavGPTv2_Inference()
            self.get_logger().info(f'推理结果: {result}')
        except Exception as e:
            self.get_logger().error(f'推理过程中发生错误: {str(e)}')
    

def main(args=None):
    """
    主函数，用于初始化和运行ROS2节点
    """

    rclpy.init(args=args)
    
    navgptv2_subscriber = NavGPTv2Subscriber()
    
    rclpy.spin(navgptv2_subscriber)
    
    navgptv2_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()