import os

PROJECT_NAME = "GCloudConsoleApp"
BUNDLE_ID = "com.yourname.gcloudconsole"
URL = "https://console.cloud.google.com/"

os.makedirs(PROJECT_NAME, exist_ok=True)

# --- 1) ViewController.swift ---

swift_code = f"""
import UIKit
import WebKit

class ViewController: UIViewController {{
    var webView: WKWebView!

    override func viewDidLoad() {{
        super.viewDidLoad()

        let config = WKWebViewConfiguration()
        webView = WKWebView(frame: view.bounds, configuration: config)
        webView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(webView)

        guard let url = URL(string: "{URL}") else {{
            return
        }}
        let request = URLRequest(url: url)
        webView.load(request)
    }}
}}
"""

with open(f"{PROJECT_NAME}/ViewController.swift", "w", encoding="utf-8") as f:
    f.write(swift_code)

# --- 2) AppDelegate.swift ---

app_delegate = f"""
import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {{

    var window: UIWindow?

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {{

        window = UIWindow(frame: UIScreen.main.bounds)
        let vc = ViewController()
        window?.rootViewController = vc
        window?.makeKeyAndVisible()

        return true
    }}
}}
"""

with open(f"{PROJECT_NAME}/AppDelegate.swift", "w", encoding="utf-8") as f:
    f.write(app_delegate)

# --- 3) Info.plist ---

plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>GCloud Console</string>
    <key>CFBundleIdentifier</key>
    <string>{BUNDLE_ID}</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>LSRequiresIPhoneOS</key>
    <true/>
    <key>UIRequiresFullScreen</key>
    <true/>
    <key>UIStatusBarHidden</key>
    <false/>
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <true/>
    </dict>
</dict>
</plist>
"""

with open(f"{PROJECT_NAME}/Info.plist", "w", encoding="utf-8") as f:
    f.write(plist)

# --- 4) إضافة ملف الأيقونة داخل المشروع ---

icon_path = f"{PROJECT_NAME}/IMG_9964.png"
if not os.path.exists(icon_path):
    with open(icon_path, "wb") as f:
        f.write(b"")  # ملف فارغ كتنبيه — ضع الأيقونة الحقيقية هنا

print("✅ تم إنشاء مشروع iOS WebView لموقع Google Cloud Console")
print("📌 ضع ملف IMG_9964.png الحقيقي داخل مجلد:", PROJECT_NAME)
