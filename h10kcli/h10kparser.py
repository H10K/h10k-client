"""h10kparser.py: Parse the H10K Config File."""
import pprint
import sys


class ParseConfig:
    """A class to check the format of the H10K config file."""

    def __init__(self, dict, filename):
        """Construct a ParseConfigFile object."""
        self.status(0)
        self.filename(filename)
        self.check_root(dict)

    def check_ambari(self, data):
        """Parse the ambari settings."""
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(data)
        mandatory = ['cluster_name', 'instance_type']
        optional = ['username', 'password']

        for key in data:
            if (key not in mandatory) and (key not in optional):
                sys.stderr.write("E030: Invalid key %s in ambari.\n" % key)
                return self.status(30)
            elif key == 'instance_type':
                self.validate_instance_type('ambari', data['instance_type'])

    def check_root(self, data):
        """Parse the top level of the configuration file."""
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(data)
        mandatory = ['ambari']

        if type(data) is not dict:
            sys.stderr.write("E010: %s doesn't seem to be valid YAML\n" %
                             self.filename())
            return self.status(10)

        for key in data:
            if key not in mandatory:
                sys.stderr.write("E020: Invalid key %s.\n" % key)
                return self.status(20)
            elif key == 'ambari':
                self.check_ambari(data['ambari'])

    def filename(self, filename=None):
        """Get/set the file name."""
        if filename is not None:
            self._filename = filename
        return self._filename

    def status(self, status=None):
        """Get/set the file name."""
        if status is not None:
            self._status = status
        return self._status

    def validate_instance_type(self, section, instance_type):
        """Check that a supplied EC2 instance type is valid."""
        ec2_instance_type_list = [
            "t1.micro", "t2.nano", "t2.micro", "t2.small", "t2.medium",
            "t2.large", "t2.xlarge", "t2.2xlarge", "m1.small", "m1.medium",
            "m1.large", "m1.xlarge", "m3.medium", "m3.large", "m3.xlarge",
            "m3.2xlarge", "m4.large", "m4.xlarge", "m4.2xlarge", "m4.4xlarge",
            "m4.10xlarge", "m4.16xlarge", "m2.xlarge", "m2.2xlarge",
            "m2.4xlarge", "cr1.8xlarge", "r3.large", "r3.xlarge",
            "r3.2xlarge", "r3.4xlarge", "r3.8xlarge", "r4.large", "r4.xlarge",
            "r4.2xlarge", "r4.4xlarge", "r4.8xlarge", "r4.16xlarge",
            "x1.16xlarge", "x1.32xlarge", "x1e.xlarge", "x1e.2xlarge",
            "x1e.4xlarge", "x1e.8xlarge", "x1e.16xlarge", "x1e.32xlarge",
            "i2.xlarge", "i2.2xlarge", "i2.4xlarge", "i2.8xlarge", "i3.large",
            "i3.xlarge", "i3.2xlarge", "i3.4xlarge", "i3.8xlarge",
            "i3.16xlarge", "i3.metal", "hi1.4xlarge", "hs1.8xlarge",
            "c1.medium", "c1.xlarge", "c3.large", "c3.xlarge", "c3.2xlarge",
            "c3.4xlarge", "c3.8xlarge", "c4.large", "c4.xlarge", "c4.2xlarge",
            "c4.4xlarge", "c4.8xlarge", "c5.large", "c5.xlarge", "c5.2xlarge",
            "c5.4xlarge", "c5.9xlarge", "c5.18xlarge", "c5d.large",
            "c5d.xlarge", "c5d.2xlarge", "c5d.4xlarge", "c5d.9xlarge",
            "c5d.18xlarge", "cc1.4xlarge", "cc2.8xlarge", "g2.2xlarge",
            "g2.8xlarge", "g3.4xlarge", "g3.8xlarge", "g3.16xlarge",
            "cg1.4xlarge", "p2.xlarge", "p2.8xlarge", "p2.16xlarge",
            "p3.2xlarge", "p3.8xlarge", "p3.16xlarge", "d2.xlarge",
            "d2.2xlarge", "d2.4xlarge", "d2.8xlarge", "f1.2xlarge",
            "f1.16xlarge", "m5.large", "m5.xlarge", "m5.2xlarge",
            "m5.4xlarge", "m5.12xlarge", "m5.24xlarge", "h1.2xlarge",
            "h1.4xlarge", "h1.8xlarge", "h1.16xlarge"
          ]

        if type(instance_type) is not str:
            sys.stderr.write("E040: Invalid instance type %s (%s).\n" %
                             (instance_type, section))
            return self.status(40)

        if instance_type not in ec2_instance_type_list:
            sys.stderr.write("E040: Invalid instance type %s (%s).\n" %
                             (instance_type, section))
            return self.status(40)
