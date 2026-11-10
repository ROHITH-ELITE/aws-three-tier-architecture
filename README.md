# AWS Three-Tier Architecture Project

## Building Scalable, Secure, and High-Performance Web Applications with AWS

### Project Overview
This project demonstrates the implementation of a three-tier web application architecture using Amazon Web Services (AWS).

The application uses a Python Flask backend, an Amazon RDS MySQL database, and an Application Load Balancer to distribute incoming web traffic across web server instances.

### Architecture

The project consists of three layers:

1. **Web Tier:** Amazon EC2 instances running Nginx.
2. **Application Tier:** Python Flask application running on an EC2 instance.
3. **Database Tier:** Amazon RDS MySQL database.

### AWS Services Used
- Amazon VPC
- Public and Private Subnets
- Amazon EC2
- Amazon RDS (MySQL)
- Application Load Balancer (ALB)
- Auto Scaling Group
- Launch Template
- Security Groups
- Amazon Machine Image (AMI)

### Project Configuration
- AWS Region: Asia Pacific (Sydney) – ap-southeast-2
- VPC CIDR: 10.0.0.0/16
- Six subnets across two Availability Zones
- Two web server instances
- Flask application running on port 8080
- Nginx reverse proxy
- MySQL database
- Auto Scaling Group with minimum capacity 1 and maximum capacity 2
- Target tracking policy based on average CPU utilization (50%)

### Application Features
- Application health check
- MySQL database connectivity
- Visitor registration
- Visitor records retrieval
- Load-balanced web application access

### Testing Results
The following tests were successfully completed:

- Application health endpoint returned a healthy status.
- Database connectivity test succeeded.
- Visitor records were successfully retrieved from MySQL.
- Application Load Balancer was Active.
- Both registered web targets were Healthy.
- Auto Scaling Group successfully launched its web instance.

### API Endpoints

| Endpoint | Description |
|---|---|
| `/api/health` | Application health check |
| `/api/db-test` | Database connectivity test |
| `/api/visitors` | Retrieve visitor records |
| `/api/visitors` (POST) | Register a visitor |

### Project Objective
The objective is to understand and implement a scalable, highly available, and database-connected web application using AWS cloud infrastructure.

### Author
Rohith Sriram

### Technologies
Python | Flask | MySQL | Nginx | AWS | Linux
