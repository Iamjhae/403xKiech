<p align="center">
  <img src="https://raw.githubusercontent.com/YOURNAME/403x/main/assets/banner.png" width="800">
</p>
<h1 align="center">403x</h1>
<p align="center">
Advanced 403 Bypass Recon Framework for Bug Bounty Hunters
</p>

 
 ███████╗ ██████╗ ██████╗ ██╗  ██╗██╗  ██╗
 ██╔════╝██╔═══██╗██╔══██╗╚██╗██╔╝╚██╗██╔╝
 █████╗  ██║   ██║██████╔╝ ╚███╔╝  ╚███╔╝
 ██╔══╝  ██║   ██║██╔══██╗ ██╔██╗  ██╔██╗
 ██║     ╚██████╔╝██║  ██║██╔╝ ██╗██╔╝ ██╗
 ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

      Advanced 403 Bypass Recon Framework

🚀 Overview
403x is a high-performance reconnaissance and security testing framework designed to identify HTTP 403 (Forbidden) access control bypass vulnerabilities in web applications.
During bug bounty hunting and penetration testing, it is common to encounter protected endpoints such as:      
```
/admin
/internal
/api/private
/dashboard
```
These endpoints often return a 403 Forbidden response, but due to misconfigured reverse proxies, load balancers, or access control mechanisms, they can sometimes be bypassed using specially crafted requests.

403x automates the discovery and testing of these weaknesses by executing hundreds of bypass techniques against protected endpoints.

The tool is built specifically for bug bounty hunters and security researchers and integrates smoothly with popular security tools like:
```
Burp Suite
ffuf
Subfinder
Nuclei
```
Features
🔎 Automatic Endpoint Discovery
Automatically scans common sensitive paths such as:
```
/admin
/dashboard
/console
/internal
/api/private
```
🚧 403 Detection Engine
Detects endpoints returning:
```
401 Unauthorized
403 Forbidden
```
Then automatically attempts bypass techniques.

🧠 Smart Bypass Detection
Automatically flags responses that indicate possible bypass:
200 OK
201 Created
202 Accepted
204 No Content
301 Redirect
302 Redirect

⚙️ Multi-threaded Scanning
High-performance scanning using configurable thread counts for faster testing.

🔁 Proxy Support
Supports interception proxies like:
Burp Suite
Allowing security researchers to inspect and modify bypass attempts.

📄 Output Export
Export results for reporting:
```
bypass_results.txt
```

📦 Installation
Clone the repository:
```
git clone https://github.com/YOURNAME/403xKiech.git
cd 403xKiech
```

Install dependencies:
```
pip install -r requirements.txt
```
Or install globally:
```
pip install .
```
Run the tool:
```
403x -u https://target.com/admin
```
⚙️ Usage
Basic scan:
```
403x -u https://target.com/admin
```
Scan a full domain and auto-discover endpoints:
```
403x -u https://target.com
```
Run with custom thread count:
```
403x -u https://target.com/admin -t 50
```
Save results:
```
403x -u https://target.com/admin -o results.txt
```

🔍 Using With Burp Suite
Start Burp Suite and enable the proxy:
```
127.0.0.1:8080
```
Run:
```
403x -u https://target.com/admin -p http://127.0.0.1:8080
```
All bypass attempts will now pass through Burp for inspection.

🧪 Example Output
```
[403 FOUND] https://target.com/admin
[403 FOUND] https://target.com/internal

[BYPASS SUCCESS]
https://target.com/admin/.

[BYPASS SUCCESS]
https://target.com/admin%20
🛠 Bug Bounty Workflow
```
Typical reconnaissance pipeline:
subdomain discovery
      ↓
endpoint discovery
      ↓
403x bypass scanning
      ↓
directory fuzzing
      ↓
vulnerability scanning

Tools commonly used:
Subfinder
httpx
ffuf
Nuclei

⚠️ Disclaimer
This tool is intended strictly for authorized security testing and educational purposes.
The developers are not responsible for misuse or illegal activities performed with this tool.
Always ensure you have explicit permission before scanning any target.

⭐ Support the Project
If you find 403x useful:
⭐ Star the repository
🐛 Report issues
🔧 Contribute improvements on GitHub.

👨‍💻 Author
Arookiech
Security Researcher | Bug Bounty Hunter

🔥 Future Roadmap
Upcoming features:
Automatic subdomain discovery (Censys + SecurityTrails API)
JavaScript endpoint extraction
Async scanning engine (10x faster)
Advanced WAF bypass detection
Automated bug bounty recon pipeline
```
Update the payload first in 403xKiech/payload.txt to suite your taste
```
