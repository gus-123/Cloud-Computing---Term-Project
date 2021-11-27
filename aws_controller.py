import boto3
from botocore.exceptions import ClientError

access_key = "key"   
secret_key = "key"   
region = "us-east-2"
 
def AWS_VM(num):
    
    
    ec2 = boto3.resource('ec2', aws_access_key_id = access_key, aws_secret_access_key = secret_key, region_name = region)

    
    ## List Instances ##
    if num == 1:
        print('[AWS EC2 List Instances]')
        VmList = ec2.instances.all()
        count_vm = 1
        for instance in VmList:
            print("[{0}] id=({1}), type=({2}), state=({3})".format(str(count_vm), instance.id, instance.instance_type, instance.state['Name']))
            count_vm += 1

    
    ## Available Zones ##
    elif num == 2:
        print('[AWS EC2 Available Zones]')
        response = ec2.describe_availability_zones()
        print('Availability Zones : ', response['AvailabilityZones'])
    
    
    ## Start Instance ##
    elif num == 3:
        print('[AWS EC2 Start Instance]')

 
    ## Available Regions ##
    elif num == 4:
        print('[AWS EC2 Available Regions]')
        response = ec2.describe_regions()
        print('Available Regions : ', response['Regions'])


    ## Stop Instance ##
    elif num == 5:
        print('[AWS EC2 Stop Instance]')
    
    
    ## Create Instance ##
    elif num == 6:
        print('[AWS EC2 Create Instance]')
        
        
    ## Reboot Instance ##
    elif num == 7:
        print('[AWS EC2 Reboot Instance]')
        
    
    ## list Images ##
    elif num == 8:
        print('[AWS EC2 list Instance]')
        
        
        


def main():
    
    
    print()
    print("------------------------------------------------------------");
    print("  1. list instance                2. available zones        ");
    print("  3. start instance               4. available regions      "); 
    print("  5. stop instance                6. create instance        "); 
    print("  7. reboot instance              8. list images            "); 
    print("                                 99. quit                   ");
    print("                                                            ");
    print("                      Created By kIM Hyun-Min on 2021.11.18 ");
    print("------------------------------------------------------------");
    print()
    while True:
        InputGet = input('cli> ')
        
        # ----- list instance ----- 
        if '1' == InputGet :
            AWS_VM(1)
           
        # ----- available zones -----    
        if '2' == InputGet :
            AWS_VM(2)
            
        # ----- start instance ----- 
        if '3' == InputGet :
            AWS_VM(3)
            
        # ----- available regions -----
        if '4' == InputGet :
            AWS_VM(4)
            
        # ----- stop instance ----- 
        if '5' == InputGet :
            AWS_VM(5)
        
        # ----- create instance -----
        if '6' == InputGet :
            AWS_VM(6)
            
        # ----- reboot instance -----
        if '7' == InputGet :
            AWS_VM(7)
            
        # ----- list images -----
        if '8' == InputGet :
            AWS_VM(8)
            
        # ----- quit ----- 
        if '99' == InputGet :
            break
            
        else :
            print('Wrong Integer.')

main()
