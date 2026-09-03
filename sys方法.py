import sys
import socket

class SysScan:
    def __init__(self):
        self.version = "1.0.0"
        self.default_port = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445,
                             1433, 1521, 3306, 3389, 5432, 6379, 8080]

    def is_open(self, ip, port):
        """
        判断端口是否开放
        :param ip: 主机ip地址
        :param port: 端口
        :return: True/False
        """
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # 默认也是这个, 所以括号内不写也可以
        sk.settimeout(0.5)      # 超时, 避免因端口无响应阻塞过久
        try:
            sk.connect((ip, port))
            return True
        except:
            return False
        finally:
            sk.close()      # 无论成功失败，最后一定关闭套接字, 避免资源泄露

    def scan(self, ip, portlist):
        """
        扫描默认端口
        :param ip: 主机ip地址
        :param portlist: 默认端口列表
        """
        for port in portlist:
            if self.is_open(ip, port):
                print(f"主机 {ip} 的端口 {port} open")
            else:
                print(f"主机 {ip} 的端口 {port} close")

    def rscan(self, ip, s, d):
        """
        自定义端口范围进行扫描
        :param ip: 主机ip地址
        :param s: source, 端口号起始位置
        :param d: destination, 端口号结束位置
        """
        if s > d:
            print("端口起始数字必须小于结束数字，请检查!")
            return
        for port in range(s, d+1):
            if self.is_open(ip, port):
                print(f"主机 {ip} 的端口 {port} open")
            else:
                print(f"主机 {ip} 的端口 {port} close")

    def is_valid_ip(self, ip):
        """
        判断ip地址是否合法
        :param ip: 主机ip地址
        :return: True/False
        """
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            try:
                num = int(part)
                if num < 0 or num > 255:
                    return False
            except:
                return False
        return True

    def is_valid_port(self, port_range):
        """
        判断端口是否合法
        :param port_range: 端口号列表
        :return: True/False
        """
        try:
            for p in port_range:
                port = int(p)
                if not (0 <= port <= 65535):
                    return False
            return True
        except:
            return False

    def cscan(self, ip, *args):
        """
        选择端口进行扫描
        :param ip: 主机ip地址
        :param args: 可变数量的端口号
        """
        for port in args:
            if self.is_open(ip, port):
                print(f"主机 {ip} 的端口 {port} open")
            else:
                print(f"主机 {ip} 的端口 {port} close")

    def main(self):
        """
        功能: 寻求帮助文档命令, 寻求程序版本号, 扫描默认端口, 选择端口进行扫描, 自定义端口范围进行扫描
        """
        if len(sys.argv) == 2:
            # 寻求帮助文档命令
            if sys.argv[1] in ["-h", "--help"]:
                print("python sys方法.py <ip> ------ 扫描默认端口")
                print("python sys方法.py <ip> <port_range> ------ 自定义端口范围进行扫描 (例如扫描81至85号端口: python sys方法.py 127.0.0.1 81-85)")
                print("python sys方法.py <ip> <port_list> ------ 选择端口进行扫描 (例如扫描81和83端口: python sys方法.py 127.0.0.1 81,83)")

            # 寻求程序版本号
            elif sys.argv[1] in ["-v", "--version"]:
                print(f"程序版本号为{self.version}")
            # 扫描默认端口
            elif self.is_valid_ip(sys.argv[1]):
                self.scan(sys.argv[1], self.default_port)
            else:
                print("非法输入, 请使用帮助文档检查! (例: python sys方法.py -h 或 python sys方法.py --help)")
        elif len(sys.argv) == 3:
            # 选择端口进行扫描
            if "," in sys.argv[2]:
                port_list = sys.argv[2].split(",")
                if self.is_valid_ip(sys.argv[1]) and self.is_valid_port(port_list):
                    self.cscan(sys.argv[1], *[int(p) for p in port_list])
                else:
                    print("IP地址或端口号非法, 请检查!")
            # 自定义端口范围进行扫描
            elif "-" in sys.argv[2]:
                port_range = sys.argv[2].split("-")
                if self.is_valid_ip(sys.argv[1]) and self.is_valid_port(port_range):
                    s = int(port_range[0])
                    d = int(port_range[1])
                    self.rscan(sys.argv[1], s, d)
                else:
                    print("IP地址或端口号非法, 请检查!")
            else:
                print("非法输入, 请使用帮助文档检查! (例: python sys方法.py -h 或 python sys方法.py --help)")
        else:
            print("非法输入, 请使用帮助文档检查! (例: python sys方法.py -h 或 python sys方法.py --help)")

# python sys方法.py 127.0.0.1
if __name__ == "__main__":
    sys_test = SysScan()
    sys_test.main()









