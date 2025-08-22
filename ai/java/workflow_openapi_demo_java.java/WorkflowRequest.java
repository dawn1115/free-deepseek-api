import javax.net.ssl.HttpsURLConnection;
import java.io.*;
import java.net.URI;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class WorkflowRequest {

    public static void main(String[] args) throws Exception {
        String apiKey = "2563e7415939bf27e627edc78f2ce83a";
        String apiSecret = "YWY3OTU0MjI0NjM5NzRiMjUwMDI5MjNj";

        String urlString = "https://xingchen-api.xf-yun.com/workflow/v1/chat/completions";
        URL url = URI.create(urlString).toURL();
        HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();

        // 配置 SSL（如果需要跳过证书验证，可以配置 TrustManager）
        conn.setSSLSocketFactory((HttpsURLConnection.getDefaultSSLSocketFactory()));
        conn.setRequestMethod("POST");
        conn.setConnectTimeout(120_000);
        conn.setReadTimeout(120_000);

        // 设置 headers
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("Accept", "text/event-stream");
        conn.setRequestProperty("Authorization", "Bearer " + apiKey + ":" + apiSecret);
        conn.setDoOutput(true);

        // 获取用户输入
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入要发送的内容: ");
        String userInput = scanner.nextLine();
        scanner.close();
        
        // 如果用户没有输入，使用默认值
        if (userInput.trim().isEmpty()) {
            userInput = "你好";
            System.out.println("使用默认内容: " + userInput);
        }

        // 构造 JSON 数据
        String payload = String.format("""
                {
                    "flow_id": "7361279241469214722",
                    "uid": "123",
                    "parameters": {"AGENT_USER_INPUT": "%s"},
                    "ext": {"bot_id": "adjfidjf", "caller": "workflow"},
                    "stream": false
                }
                """, userInput);

        // 发送请求体
        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = payload.getBytes(StandardCharsets.UTF_8);
            os.write(input);
        }

        // 读取 stream 参数，决定是否分段读取
        boolean stream = false; // 你可以改成 true 看效果
        if (stream) {
            try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                String line;
                while ((line = br.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } else {
            try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                String response = br.readLine();
                System.out.println(response);
            }
        }

        conn.disconnect();
    }
}