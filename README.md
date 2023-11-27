# Random Cat Generator

## Overview
Random Cat Generator is a serverless application built on AWS Lambda and API Gateway, utilizing the Cat as a Service (CATAAS) API. It provides a simple web interface to display random cat images, making every user's experience unique and delightful.

## Features
- **Serverless Architecture:** Utilizes AWS Lambda for backend logic, ensuring scalability and cost-effectiveness.
- **API Gateway Integration:** Seamlessly connects the Lambda function to a web interface.
- **Random Cat Images:** Fetches random cat images tagged 'cute' from the CATAAS API.

## How It Works
Upon receiving a request, the Lambda function contacts the CATAAS API and retrieves a list of cat images. It then randomly selects an image and returns an HTML response displaying this image.

## Prerequisites
- AWS Account
- Basic understanding of AWS Lambda and API Gateway
- Familiarity with Python

## Setup and Deployment
1. **Create a Lambda Function:**
   - Navigate to AWS Lambda and create a new function.
   - Use Python 3.8 (or a version of your choice) as the runtime.
   - Paste the provided Python script into the Lambda code editor.
   - Save and deploy the Lambda function.

2. **Configure API Gateway:**
   - Create a new API in Amazon API Gateway.
   - Set up a new resource and a GET method linked to your Lambda function.
   - Deploy the API to a new stage (e.g., 'prod').

3. **Access the Application:**
   - Use the Invoke URL provided by API Gateway to access the web application.

## Usage
Simply navigate to the provided Invoke URL. You will be greeted with a random cat image on each visit or page refresh.

## Security and Permissions
- Ensure that your Lambda function has the necessary permissions to access the CATAAS API.
- Follow best practices for securing your API Gateway endpoint.

## Contributions
Contributions to the Random Cat Generator are welcome. Please ensure that you test your changes thoroughly before submitting a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Cat as a Service (CATAAS) API for providing cat images.
- AWS for serverless architecture solutions.
