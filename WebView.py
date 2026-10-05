import os
import json

PROJECT = "GCloudConsoleApp"
APP_NAME = "GCloudConsole"
BUNDLE_ID = "com.yourname.gcloudconsole"
URL = "https://console.cloud.google.com/"

os.makedirs(PROJECT, exist_ok=True)

# -----------------------------
# 1) Swift Files
# -----------------------------

view_controller = f"""
import UIKit
import WebKit

class ViewController: UIViewController {{
    override func viewDidLoad() {{
        super.viewDidLoad()

        let webView = WKWebView(frame: view.bounds)
        webView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        view.addSubview(webView)

        let url = URL(string: "{URL}")!
        webView.load(URLRequest(url: url))
    }}
}}
"""

app_delegate = """
import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        window = UIWindow(frame: UIScreen.main.bounds)
        window?.rootViewController = ViewController()
        window?.makeKeyAndVisible()

        return true
    }
}
"""

with open(f"{PROJECT}/ViewController.swift", "w") as f:
    f.write(view_controller)

with open(f"{PROJECT}/AppDelegate.swift", "w") as f:
    f.write(app_delegate)

# -----------------------------
# 2) Info.plist
# -----------------------------

plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>{APP_NAME}</string>
    <key>CFBundleIdentifier</key>
    <string>{BUNDLE_ID}</string>
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

with open(f"{PROJECT}/Info.plist", "w") as f:
    f.write(plist)

# -----------------------------
# 3) Xcode Project Structure
# -----------------------------

xcodeproj = {
    "project": {
        "name": APP_NAME,
        "bundle_id": BUNDLE_ID,
        "sources": [
            "AppDelegate.swift",
            "ViewController.swift"
        ],
        "plist": "Info.plist"
    }
}

with open(f"{PROJECT}/project.json", "w") as f:
    json.dump(xcodeproj, f, indent=4)

# -----------------------------
# 4) Build Script (No Xcode)
# -----------------------------

build_script = """
#!/bin/bash
ios-build-tools build project.json --output GCloudConsole.ipa
"""

with open(f"{PROJECT}/build.sh", "w") as f:
    f.write(build_script)

os.chmod(f"{PROJECT}/build.sh", 0o755)

print("✅ تم إنشاء مشروع iOS كامل")
print("📦 لتجميعه إلى IPA:")
print("1) ثبت ios-build-tools")
print("2) شغّل: ./build.sh")
