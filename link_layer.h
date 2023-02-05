#ifndef LINK_LAYER_H
#define LINK_LAYER_H

#include <cstdint>
#include <vector>
#include <string>

using namespace std;

class LinkLayer {
public:
    // constructor
    LinkLayer(int link_speed, bool duplex_mode, std::string device_name);

    // destructor
    ~LinkLayer();

    // send data over the physical link
    void send_data(const std::vector<uint8_t>& data);

    // receive data from the physical link
    std::vector<uint8_t> receive_data();

    // set physical link properties, such as speed and duplex mode
    void set_link_properties(int speed, bool duplex_mode);

    // get physical link properties
    int get_link_speed() const;
    bool get_duplex_mode() const;

private:
    int m_link_speed;
    bool m_duplex_mode;
    string m_device_name;
};

#endif // LINK_LAYER_H