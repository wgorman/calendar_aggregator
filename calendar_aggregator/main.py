from .meetup.meetup import downloadMeetupEvents
def main():
    print("Hello, World!")

if __name__ == "__main__":
    events = downloadMeetupEvents('https://www.meetup.com/orlandopreneur/events/')
    print('Found ', len(events), ' events')
    print(events)