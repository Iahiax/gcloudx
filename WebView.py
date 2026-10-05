import os

project = "gcloud"
os.makedirs(project, exist_ok=True)

# Swift WebView code
swift_code = """
import UIKit
import WebKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        let webView = WKWebView(frame: view.bounds)
        view.addSubview(webView)
        let url = URL(string: "https://console.cloud.google.com/")!
        webView.load(URLRequest(url: url))
    }
}
"""

with open(f"{project}/ViewController.swift", "w") as f:
    f.write(swift_code)

# info.plist
plist = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>Metrony</string>
    <key>CFBundleIdentifier</key>
    <string>com.yourname.metrony</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>LSRequiresIPhoneOS</key>
    <true/>
    <key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <true/>
    </dict>
</dict>
</plist>
"""

with open(f"{project}/Info.plist", "w") as f:
    f.write(plist)

print("تم إنشاء مشروع WebView جاهز.")
