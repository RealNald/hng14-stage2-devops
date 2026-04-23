# ---------- Builder ----------
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install --omit=dev

# ---------- Final ----------
FROM node:18-alpine

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app
# Copy only necessary files from builder
COPY --from=builder --chown=appuser:appgroup /app/node_modules ./node_modules

# Copy only your source code (not everything from host)
COPY --chown=appuser:appgroup app.js ./
COPY --chown=appuser:appgroup views ./views
# Install curl for healthcheck
RUN apk add --no-cache curl

#HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
#  CMD curl -f http://localhost:3000/health || exit 1

USER appuser
EXPOSE 3000
CMD ["node", "app.js"]
