### **Next Steps**
1. **Restart your FastAPI server** and check `http://127.0.0.1:8000/docs` again.
2. Your endpoints should now be grouped under **"Nmap Devices"** instead of "default."

### **Naming & Organization for Future Expansion**
Since you're planning to add **Nmap Services** and already have **Nmap Devices**, consider the following structure:
- **Controller files:**
  - `nmap_device_controller.py`
  - `nmap_service_controller.py`
- **Models:**
  - `nmap_scan_data.py` (Devices)
  - `nmap_service_data.py` (Services)
- **Schemas:**
  - `nmap_device_schema.py`
  - `nmap_service_schema.py`
- **API Routing:**
  - `/nmap/devices/` → Manages devices
  - `/nmap/services/` → Manages network services

This structure keeps the API modular and scalable. 🚀 