import pulumi
import pulumi_openstack as openstack
from userdata import userdata_web

openstack_provider = openstack.Provider("openstack")
resource_opts = pulumi.ResourceOptions(provider=openstack_provider)

# >>>> SecGroup <<<<

aurora_sec_group = openstack.compute.SecGroup(
    "sec-group-1",
    description="a security group",
    opts=resource_opts,
)

sec_group_rule_ssh = openstack.networking.SecGroupRule(
    "sec-rule-1",
    direction="ingress",
    ethertype="IPv4",
    port_range_max=22,
    port_range_min=22,
    protocol="tcp",
    remote_ip_prefix="0.0.0.0/0",
    description="Allow ssh",
    security_group_id=aurora_sec_group.id,
    opts=resource_opts,
)

sec_group_rule_mail_inbound_1 = openstack.networking.SecGroupRule(
    "mail-inbound-1",
    direction="ingress",
    ethertype="IPv4",
    port_range_max=25,
    port_range_min=25,
    protocol="tcp",
    remote_ip_prefix="0.0.0.0/0",
    description="Allow inbound SMTP traffic",
    security_group_id=aurora_sec_group.id,
    opts=resource_opts,
)

sec_group_rule_mail_inbound_2 = openstack.networking.SecGroupRule(
    "mail-inbound-2",
    direction="ingress",
    ethertype="IPv4",
    port_range_max=465,
    port_range_min=465,
    protocol="tcp",
    remote_ip_prefix="0.0.0.0/0",
    description="Allow inbound SMTP traffic",
    security_group_id=aurora_sec_group.id,
    opts=resource_opts,
)

sec_group_rule_mail_outbound_1 = openstack.networking.SecGroupRule(
    "mail-outbound-1",
    direction="egress",
    ethertype="IPv4",
    port_range_max=25,
    port_range_min=25,
    protocol="tcp",
    remote_ip_prefix="0.0.0.0/0",
    description="Allow outbound SMTP traffic",
    security_group_id=aurora_sec_group.id,
    opts=resource_opts,
)

sec_group_rule_mail_outbound_2 = openstack.networking.SecGroupRule(
    "mail-outbound-2",
    direction="egress",
    ethertype="IPv4",
    port_range_max=465,
    port_range_min=465,
    protocol="tcp",
    remote_ip_prefix="0.0.0.0/0",
    description="Allow outbound SMTP traffic",
    security_group_id=aurora_sec_group.id,
    opts=resource_opts,
)
#
# sec_group_rule_tls = openstack.networking.SecGroupRule(
#     "sec-rule-3",
#     direction="ingress",
#     ethertype="IPv4",
#     port_range_max=443,
#     port_range_min=443,
#     protocol="tcp",
#     remote_ip_prefix="0.0.0.0/0",
#     description="Allow external access to port 443",
#     security_group_id=aurora_sec_group.id,
#     opts=resource_opts,
# )

# sec_group_rule_rcp = openstack.networking.SecGroupRule(
#     "sec-rule-4",
#     direction="ingress",
#     ethertype="IPv4",
#     port_range_max=8050,
#     port_range_min=8050,
#     protocol="tcp",
#     remote_ip_prefix="0.0.0.0/0",
#     description="Allow external access to port 8050",
#     security_group_id=aurora_sec_group.id,
#     opts=resource_opts,
# )

# >>>> network <<<<

internal_network_1 = openstack.networking.Network("kinesis_internal", opts=resource_opts)

subnet_1 = openstack.networking.Subnet(
    "subnet-1",
    network_id=internal_network_1.id,
    cidr="192.168.199.0/24",
    ip_version=4,
    opts=resource_opts,
)

public_network = openstack.networking.get_network(name="public")

router1 = openstack.networking.Router(
    "router-1",
    external_network_id=public_network.id,
    admin_state_up=True,
    opts=resource_opts,
)

router_interface_a = openstack.networking.RouterInterface(
    "router-interface-a",
    router_id=router1.id,
    subnet_id=subnet_1.id,
    opts=resource_opts,
)

# >>>> instances <<<<

floating_ip = openstack.networking.FloatingIp(
    "my-floating-ip", pool="public", opts=resource_opts
)

aurora = openstack.compute.Instance(
    "aurora_main",
    name="aurora_main",
    flavor_name="c5.large",
    image_name="debian-12-x86_64",
    security_groups=[aurora_sec_group.name],
    networks=[
        openstack.compute.InstanceNetworkArgs(uuid=internal_network_1.id),
    ],
    user_data=userdata_web,
    opts=resource_opts,
)

floating_ip_association = openstack.compute.FloatingIpAssociate(
    "my-floating-ip-association",
    floating_ip=floating_ip.address,
    instance_id=aurora.id,
    opts=resource_opts,
)

pulumi.export("instance_ip", aurora.access_ip_v4)
pulumi.export("floating_ip", floating_ip.address)
