wireguard = open("wgconf.txt")

#empty dictionary to store raw variables
env = {}

# read in and parse the original file
for line in wireguard:
    k = line.split('=', 1)
    if len (k) >= 2:
        variable_name = k[0].strip()
        variable_value = k[1].strip()
        env[variable_name] = variable_value

wireguard.close()

# perform specific adjustments
del(env['AllowedIPs'])

mixed_address = env['Address']
Address = mixed_address.split(',')[0]
env['Address'] = Address

mixed_endpoint = env['Endpoint']
Endpoint, EndpointPort = mixed_endpoint.split(':')
env['Endpoint'] = Endpoint
env['EndpointPort'] = EndpointPort

mixed_DNS = env['DNS']
env['DNS'] = mixed_DNS.split(',')[0]


# write the variables to an env file
keys = env.keys()
keys = sorted(keys)

env_file = open('.env', 'w')
env_line = '{0}="{1}"\n'
for k in keys:
    env_file.write(env_line.format(k, env[k]))
