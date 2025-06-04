# Use a base Python image with alpine lightweight OS
FROM python:3.10-alpine

# Add a non-root user 'username' with UID 1001 and GID 1001
RUN addgroup -S -g 1001 developer && \
    adduser -S -u 1001 -G developer developer && \
    apk update && \
    apk add libmagic curl && \
    rm -rf /var/cache/apk/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /usr/local/src/app/

# Copy application code into the container
COPY . .

# Change ownership to technostore
RUN chown -R developer:developer /usr/local/src/app/

RUN chown -R developer:developer /usr/local/src/app/logs/

# Switch to the 'technostore' user
USER developer

# Create and activate a virtual environment within the user's home directory
RUN python -m venv /home/developer/venv
ENV PATH="/home/developer/venv/bin:$PATH"

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements_my.txt
# Expose port 8001
EXPOSE 8000

# Start Gunicorn
CMD ["/home/developer/venv/bin/gunicorn", "--bind", "172.22.0.2:8000", "femme.wsgi:application"]

# Healthcheck: wait for 5 seconds and attempt to access the application
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -k -f https://172.22.0.2:8000/ || (echo "Health check failed" >> /usr/local/src/app/logs/healthcheck.log && exit 1)
# Metadata labels
LABEL maintainer="Dev4Development <abdulrahim@techno.academy>" \
    version="1.1.6" \
    description="Project Femme"
