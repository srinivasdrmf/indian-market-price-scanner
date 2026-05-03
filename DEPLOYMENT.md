# Deployment Guide - Indian Market Price Scanner

## 📋 Table of Contents
1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Railway.app Deployment](#railwayapp-deployment)
4. [AWS Deployment](#aws-deployment)
5. [Heroku Deployment](#heroku-deployment)
6. [DigitalOcean Deployment](#digitalocean-deployment)

---

## Local Development

### Prerequisites
- Python 3.8+
- pip or conda
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/srinivasdrmf/indian-market-price-scanner.git
cd indian-market-price-scanner

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the scanner
python main.py
```

### Output
- Reports generated in `output/` directory
- Logs available in `logs/scanner.log`

---

## Docker Deployment

### Prerequisites
- Docker installed and running
- Docker Compose (optional)

### Build & Run

```bash
# Build Docker image
docker build -t indian-price-scanner:latest .

# Run container
docker run -v $(pwd)/output:/app/output \
           -v $(pwd)/logs:/app/logs \
           --name price-scanner \
           indian-price-scanner:latest
```

### Docker Compose (Multi-container)

```bash
docker-compose up -d
```

### Access Reports
```bash
# Copy reports from container
docker cp price-scanner:/app/output ./output
docker cp price-scanner:/app/logs ./logs
```

---

## Railway.app Deployment

### Prerequisites
- Railway.app account (https://railway.app)
- GitHub repository

### Steps

1. **Push code to GitHub**
   ```bash
   git push origin main
   ```

2. **Create Railway Project**
   - Go to https://railway.app/dashboard
   - Click "New Project"
   - Connect GitHub repository
   - Select `indian-market-price-scanner`

3. **Configure Environment**
   - Railway automatically detects Dockerfile
   - No additional configuration needed

4. **Deploy**
   - Railway builds and deploys automatically
   - Monitor logs in Railway dashboard

5. **Schedule Scans**
   - Use Railway "Deploy on GitHub push"
   - Or use cron jobs in Railway (premium)

### Cost
- Free tier: 5GB bandwidth/month
- Premium: $5-20/month

---

## AWS Deployment

### Option 1: EC2 + Docker

```bash
# 1. Launch EC2 instance (Ubuntu 20.04)
# 2. SSH into instance
ssh -i your-key.pem ec2-user@your-instance-ip

# 3. Install Docker
sudo apt-get update
sudo apt-get install docker.io docker-compose -y

# 4. Clone and deploy
git clone https://github.com/srinivasdrmf/indian-market-price-scanner.git
cd indian-market-price-scanner
sudo docker-compose up -d

# 5. Monitor
sudo docker logs -f $(sudo docker ps -q)
```

### Option 2: AWS Lambda + EventBridge

1. **Package application** for Lambda (requires serverless framework)
2. **Configure EventBridge** to trigger daily/hourly
3. **Store results** in S3

### Option 3: AWS Batch

1. Create Docker image and push to ECR
2. Create Batch job definition
3. Create Compute environment
4. Schedule with CloudWatch Events

### Estimated Cost
- EC2 t3.micro: ~$10/month
- Lambda: ~$0-5/month (pay per execution)
- Storage (S3): ~$0.023/GB

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Steps

```bash
# 1. Login to Heroku
heroku login

# 2. Create Heroku app
heroku create your-app-name

# 3. Push Docker container
heroku container:push web
heroku container:release web

# 4. View logs
heroku logs --tail

# 5. Schedule with Heroku Scheduler
heroku addons:create scheduler:standard
heroku scheduler
```

### Procfile Configuration
```
web: python main.py
worker: python main.py
```

### Cost
- Paid dynos start at $7/month
- Scheduler: Free (basic) to $250/month (advanced)

---

## DigitalOcean Deployment

### Droplet Setup

```bash
# 1. Create Ubuntu 20.04 droplet ($5-6/month)
# 2. SSH into droplet
ssh root@your-droplet-ip

# 3. Install dependencies
apt-get update
apt-get install -y python3-pip python3-venv git docker.io docker-compose

# 4. Clone and run
git clone https://github.com/srinivasdrmf/indian-market-price-scanner.git
cd indian-market-price-scanner

# 5. Create systemd service
sudo nano /etc/systemd/system/price-scanner.service
```

### Systemd Service File
```ini
[Unit]
Description=Indian Price Scanner
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/indian-market-price-scanner
ExecStart=/usr/bin/python3 /root/indian-market-price-scanner/main.py
Restart=always
RestartSec=300

[Install]
WantedBy=multi-user.target
```

### Enable and Start
```bash
sudo systemctl daemon-reload
sudo systemctl enable price-scanner
sudo systemctl start price-scanner
```

### Cost
- Basic Droplet: $5/month
- Database (PostgreSQL): $15/month
- Spaces (Storage): $5/month

---

## Environment Variables

Create `.env` file for sensitive data:

```bash
# .env
DISCOUNT_THRESHOLD=0.80
CHECK_INTERVAL=3600
LOG_LEVEL=INFO
OUTPUT_DIR=./output
```

---

## Monitoring & Logging

### Local
```bash
tail -f logs/scanner.log
```

### Cloud Platforms
- **Railway**: Built-in dashboard logs
- **AWS CloudWatch**: Automatic log aggregation
- **Heroku**: `heroku logs --tail`
- **DigitalOcean**: SSH and check systemd logs

---

## Scheduled Execution

### Cron (Local/VPS)
```bash
# Edit crontab
crontab -e

# Run daily at 2 AM
0 2 * * * cd /path/to/scanner && python main.py

# Run every 6 hours
0 */6 * * * cd /path/to/scanner && python main.py
```

### Cloud Schedulers
- **Railway**: GitHub push triggers
- **AWS**: CloudWatch Events / EventBridge
- **Heroku**: Heroku Scheduler add-on
- **DigitalOcean**: App Platform cron jobs

---

## Troubleshooting

### Docker Issues
```bash
# Check container status
docker ps -a

# View logs
docker logs container-id

# Rebuild image
docker build --no-cache -t indian-price-scanner:latest .
```

### Memory Issues
```bash
# Increase allocated memory
docker run -m 2g -e PYTHONUNBUFFERED=1 ...
```

### Network Timeouts
- Increase `timeout` in config.yaml
- Check firewall rules
- Use VPN/proxy if rate limited

---

## Best Practices

1. **Use volumes** for persistent output storage
2. **Enable health checks** for automatic restarts
3. **Monitor logs** for errors and warnings
4. **Schedule regular scans** (avoid peak hours)
5. **Backup reports** to cloud storage (S3, GCS, etc.)
6. **Use environment variables** for configuration
7. **Monitor costs** on cloud platforms
8. **Set up alerts** for failed scans

---

## Cost Comparison

| Platform | Min Cost | Pros | Cons |
|----------|----------|------|------|
| Local | Free | No cloud costs | Requires always-on server |
| Railway | Free | Easy setup, free tier | Limited free bandwidth |
| AWS EC2 | $10/mo | Scalable, reliable | Complex setup |
| Heroku | $7/mo | Simple, GitHub integration | Limited free tier |
| DigitalOcean | $5/mo | Affordable, good docs | Manual setup |
| AWS Lambda | $0-5/mo | Pay per run, scalable | Complex packaging |

---

## Support & Documentation

- [Docker Documentation](https://docs.docker.com)
- [Railway.app Docs](https://docs.railway.app)
- [AWS EC2 Guide](https://docs.aws.amazon.com/ec2)
- [Heroku Documentation](https://devcenter.heroku.com)
- [DigitalOcean Community](https://www.digitalocean.com/community)

---

**Made with ❤️ for Indian shoppers**
