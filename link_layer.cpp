#include "link_layer.h"

LinkLayer::LinkLayer(int link_speed, bool duplex_mode, std::string device_name)
   : m_link_speed(link_speed),
     m_duplex_mode(duplex_mode),
     m_device_name(device_name) {
   // Any other required initialization, but nothing for now
}


int LinkLayer::Open(const char* device) {
  // Implement here
}

int LinkLayer::Close() {
  // Implement here
}

int LinkLayer::SendFrame(const char* frame, size_t length) {
  // Implement here
}

int LinkLayer::ReceiveFrame(char* frame, size_t& length) {
  // Implement here
}

int LinkLayer::GetMacAddress(char* mac_address) {
  // Implement here
}

int LinkLayer::SetMacAddress(const char* mac_address) {
  // Implement here
}

int LinkLayer::GetMTU(size_t& mtu) {
  // Implement here
}