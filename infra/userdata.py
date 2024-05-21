userdata_web = """
#cloud-config

users:
  - name: debian
    ssh_authorized_keys:
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMHsWCIVpQBOCDcJ/J7JoxRdIbw3tOD+r4Wn+X53Fro5iCHB2MtrSBruG2g2j3wD5UqdcK+kGAkydyxnYX6OXnV1rGbE635SzVaQG2fdEoBQYlGaFWiibxSlFGueo2wzInzAXAMkVCAWtlvprjc8njASS6looydTrZ88ULx79Bznzg/fZu49wyPi1XcxRon98uw7pc30lrnoGmD55XYATL6UB8QkAIZkGZP1W5nzZSE/N5yfkgNjd6b2VLmSMnjwPYoj+NtsTmrc2YXYu4nFF0AnIENOjYnLsKrhGOiPchHwpw8dj0JQnYb8P8JMeH8/Klh7pIeYmRyKR/hxVo0Gtf27+sPVhy0Azhe1yxW8ZJIU/bi7hwtfhy1f9B6TXpwKiZIMoyVyPtEtXA7eWz4bcOpPGdUfev5HTRGjHxddOMDiQqtUx06SXsSF1YQNutioGjx7yT3Th3fTnQGktvfI0ZUIZTx6XzcD8S74orIp1QL04P0XZkmw0nDV6PuCm44F0= smeyer@Sebastians-MacBook-Pro.local
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: sudo
    shell: /bin/bash

runcmd:

  - curl -fsSL https://get.docker.com -o get-docker.sh
  - sh get-docker.sh
  - rm get-docker.sh
  - sudo apt-get update
  - sudo systemctl start docker
  
  


  
"""