
def main():
    spacecraft = {}
    # spacecraft['name'] = 'James Webb Space Telescope'
    spacecraft.update({'distance': 0.01, 'orbit': 'Sun'})
    # del spacecraft['name'] # del statement deletes a key-value pair.
    print(create_report(spacecraft))

def create_report(spacecraft):
    # Non empty dict evaluates to True and empty to False.
    if spacecraft: 
        return f"""
            ========== Report ==========

            Name: {spacecraft.get('name', 'Unknown')}
            Distance: {spacecraft.get('distance', 'Unknown')} AU
            Orbit: {spacecraft.get('orbit', 'Unknown')}
            time_elapsed: {spacecraft.get('time', 'Unknown')} H

            ==========================

        """
    else:
        print('There is no information regarding spacecraft.')

main()