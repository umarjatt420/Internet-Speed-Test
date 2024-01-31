import speedtest
import subprocess

def test_internet_speed():
    print('Please Wait...')
    st = speedtest.Speedtest()

    # Perform the speed test
    best_server = st.get_best_server()
    st.download(threads=None)
    st.upload(threads=None)

    # Get additional information
    server = best_server['host']
    sponsor = best_server['sponsor']

    # Measure packet loss using ping
    ping_result = subprocess.Popen(
        ["ping", "-c", "10", server],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    ping_output, _ = ping_result.communicate()
    packet_loss = ping_output.decode().count("time=")

    # Print the results
    print(f"Server: {server} ({sponsor})")
    print(f"Download Speed: {st.results.download / 10**6:.2f} Mbps")
    print(f"Upload Speed: {st.results.upload / 10**6:.2f} Mbps")
    print(f"Latency: {st.results.ping:.2f} ms")
    print(f"Packet Loss: {packet_loss} packets")

test_internet_speed()