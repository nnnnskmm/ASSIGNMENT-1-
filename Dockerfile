# Use Ubuntu as the base image
FROM ubuntu

# Install required packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

RUN apt-get update && apt-get install -y nano

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Copy the dataset file to the container
COPY diabetes.csv /home/doc-bd-a1/
copy load.py /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
copy model.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/
copy final.sh /home/doc-bd-a1/

# Open the bash shell upon container startup
CMD ["/bin/bash"]