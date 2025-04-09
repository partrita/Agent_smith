# Agent_smith

LLM agent for bioinformatics

## 8502 포트 열기

### **리눅스에서 포트 8502 열기**

#### **1. 포트 상태 확인**
먼저, 포트 8502가 현재 사용 중인지 확인합니다.
```bash
sudo netstat -tlnp | grep 8502  # netstat 사용 [1][2]
sudo ss -tlnp | grep 8502       # ss 사용 (더 빠름) [1]
```
- `-t`: TCP 포트 확인
- `-l`: LISTEN 상태 포트만 표시
- `-n`: 숫자로 포트 표시
- `-p`: 프로세스 정보 포함

#### **2. 방화벽 설정 (iptables)**
포트를 열기 위해 방화벽 규칙을 추가합니다.
```bash
sudo iptables -I INPUT -p tcp --dport 8502 -j ACCEPT  # TCP 허용 [1][5]
sudo iptables -I INPUT -p udp --dport 8502 -j ACCEPT  # UDP 허용 (필요 시) [2][5]
```
- **옵션 설명**:
  - `-I INPUT`: 인바운드 규칙 추가
  - `-p tcp/udp`: 프로토콜 지정
  - `--dport 8502`: 대상 포트 지정
  - `-j ACCEPT`: 트래픽 허용

#### **3. 방화벽 설정 (UFW - Ubuntu)**
UFW(Uncomplicated Firewall)를 사용하는 경우:
```bash
sudo ufw allow 8502/tcp  # TCP 허용 [1]
sudo ufw enable          # 방화벽 활성화
```

#### **4. 변경 사항 저장 및 적용**
- **iptables 규칙 저장 (CentOS/RHEL)**:
  ```bash
  sudo service iptables save
  sudo systemctl restart iptables
  ```

#### **5. 포트 테스트**
외부에서 접근 가능한지 확인:
```bash
nc -zv [서버IP] 8502  # netcat으로 테스트 [2][3]
```
- 성공 시 `Connection to [IP] 8502 port [tcp] succeeded!` 출력.

#### **6. 추가 설정 (필요 시)**
- **SELinux 비활성화 (CentOS/RHEL)**:
  ```bash
  sudo setenforce 0  # 임시 비활성화
  sudo vim /etc/selinux/config  # 영구 설정 (SELINUX=disabled)
  ```

포트 8502가 정상적으로 열렸는지 다시 확인 후, 애플리케이션(예: Streamlit)을 해당 포트로 실행합니다.

## How to use

```bash
uv sync
uv run streamlit run src/app.py
```
