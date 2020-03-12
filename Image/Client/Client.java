import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;
import java.util.concurrent.TimeUnit;

public class Client {
	private static String host = "127.0.0.1";
	private static int port = 9030;
	public Client() {}
	public Client(String host,int port) {
		this.host = host;
		this.port = port;
	}
	public static void main(String[] args) {
		String path = args[0];
		ByteBuffer bf = ByteBuffer.allocate(1024);
		SocketChannel socketChannel = null;
		try {
			socketChannel = SocketChannel.open();
			socketChannel.configureBlocking(false);
			socketChannel.connect(new InetSocketAddress(host,port));
			if(socketChannel.finishConnect()) {
				int i=0;
				while(true) {
					TimeUnit.SECONDS.sleep(1);
					byte[] data = Util.image2byte(path);
					bf.clear();
					bf.put(data);
					bf.flip();
					while(bf.hasRemaining()) {
						System.out.println(bf);
						socketChannel.write(bf);
					}
				}
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try {
				if(null!=socketChannel) {
					socketChannel.close();
				}
			}catch(IOException e) {
				e.printStackTrace();
			}
		}
	}
}
