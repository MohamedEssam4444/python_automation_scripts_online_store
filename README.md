# python_bash_automation_scripts_online_store 
You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product. Given a bunch of images and descriptions of each of the new products: 
* Upload the new products to your online store. 
* Images and descriptions should be uploaded separately, using two different web endpoints. Since this process is key to your business's success, you need to make sure that it keeps running! So:
* Run a script on your web server to monitor system health.
* Send an email with an alert if the server is ever unhealthy.
## Scenario :
* You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description.
* You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.
* You'll have to process the .txt files (named 001.txt, 002.txt, ...) in the supplier-data/descriptions/ directory and save them in a data structure so that you can then upload them via JSON. Note that all files are written in the following format, with each piece of information on its own line:
    * name
    * weight (in lbs)
    * description
* The data model in the Django application fruit has the following fields: name, weight, description and image_name. The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.
* The image_name field will allow the system to find the image associated with the fruit. Don't forget to add all fields, including the image_name! The final JSON object should be similar to:
* {"name": "Watermelon", "weight": 500, "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", "image_name": "010.jpeg"}
* Iterate over all the fruits and use post method from Python requests library to upload all the data
* Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.
* health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:
    * Report an error if CPU usage is over 80%
    * Report an error if available disk space is lower than 20%
    * Report an error if available memory is less than 500MB
    * Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

* In event of any issues detected among the ones mentioned above, an email should be sent with the following content:
    * From: automation@example.com
    * To: username@example.com
    * Subject line:
* Case
Subject line
*CPU usage is over 80%
Error - CPU usage is over 80%
*Available disk space is lower than 20%
Error - Available disk space is less than 20%
*available memory is less than 500MB
Error - Available memory is less than 500MB
*hostname "localhost" cannot be resolved to "127.0.0.1"
Error - localhost cannot be resolved to 127.0.0.1
    * E-mail Body: Please check your system and resolve the issue as soon as possible.

### Files: 
1. **changeImage.py**: to process the supplier images
2. **supplier_image_upload.py**: that takes the jpeg images from the supplier-data/images directory that you've processed previously and uploads them to the web server fruit catalog.
3. **run.py**: to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name) , To add fruit images and their descriptions from the supplier on the fruit catalog web-server, will automatically POST the fruit images and their respective description in JSON format

#### proven steps: 

1. uploading modified images to webserver :

![Screenshot from 2020-09-17 13-45-40](https://user-images.githubusercontent.com/68178003/100703295-e6d3da80-33ab-11eb-861d-0d7ca57d38b1.png)

2. uploading description of each image and matching each description to the right image on webserver:

![Screenshot from 2020-09-17 14-40-09](https://user-images.githubusercontent.com/68178003/100708440-00c5eb00-33b5-11eb-8e27-5502831c135b.png)

![Screenshot from 2020-09-17 14-39-56](https://user-images.githubusercontent.com/68178003/100703288-e20f2680-33ab-11eb-8dde-1bbcf0b3deba.png)

