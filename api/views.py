import bson.objectid
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, FundraiserForm, FundraiserUpdateForm, DonationForm
from .models import users_collection, fundraisers_collection, donations_collection
import bson

def landing(request):
    return render(request, 'landing.html')



def login(request):
    error=''
    data = {}
    isLogged = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                data = users_collection.find_one({'email': email})
                if data.get('password') == password:
                    data['userId'] = str(data['_id'])
                    isLogged = True
                
                else:
                    form = LoginForm()
                    error = 'Wrong credientials. Please try again.'
                    
            except:
                form = LoginForm()
                error = 'User not found!! Please try again.'
        else:
            form = LoginForm()
            error = 'Wrong credientials. Please try again.'
    else:
        form = LoginForm()
    
    context = {'form': form, 'isLogged': isLogged, 'data': data, 'error': error}
    return render(request, 'login.html', context)



def register(request):
    error=''
    data = {}
    isLogged = False
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usertype = form.cleaned_data['usertype']
            user = {"username": username, "email": email, "password": password, "usertype": usertype}
            result = users_collection.insert_one(user)
            isLogged = True
            data = {
            'userId': str(result.inserted_id),
            'username': username,
            'email': email,
            'password': password,
            'usertype': usertype
            }
            
        else:
            form = RegisterForm()
            error = 'Invalid form data. Please try again.'
    else:
        form = RegisterForm()
    
    context = {'form': form, 'isLogged': isLogged, 'data': data, 'error': error}
    return render(request, 'register.html', context)

def loadHome(request):
    return render(request, 'loading/loadHome.html')


def home(request, id):
    fundraisers = [fundraiser for fundraiser in fundraisers_collection.find()]
    for fundraiser in fundraisers:
        fundraiser['id'] = str(fundraiser['_id'])
    return render(request, 'user/home.html', {'fundraisers': fundraisers, "id": id})


def loadNewFundraiser(request):
    return render(request, 'loading/loadNewfunding.html')

def newFundraiser(request, id):
    success = False
    error = ''
    if request.method == 'POST':
        form = FundraiserForm(request.POST)
        if form.is_valid():
            print("valid")
            applicantId = id
            applicantName = form.cleaned_data['applicantName']
            applicantEmail = form.cleaned_data['applicantEmail']
            applicantMobile = form.cleaned_data['applicantMobile']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            bannerImage = form.cleaned_data['bannerImage']
            purpose = form.cleaned_data['purpose']
            deadline = form.cleaned_data['deadline']
            targetAmount = form.cleaned_data['targetAmount']
            extraImage1 = form.cleaned_data['extraImage1']
            extraImage2 = form.cleaned_data['extraImage2']
            extraImage3 = form.cleaned_data['extraImage3']

            fundraiser = {"applicantId": applicantId, "applicantName": applicantName, "applicantEmail": applicantEmail, "applicantMobile": applicantMobile, "title": title,
                          "description": description, "bannerImage": bannerImage, "purpose": purpose, "deadline": deadline, "targetAmount": targetAmount, "collectedAmount": 0,
                          "extraImage1": extraImage1, "extraImage2": extraImage2,"extraImage3": extraImage3,}
            print(fundraiser)
            result = fundraisers_collection.insert_one(fundraiser)
            print(result)
            success = True

  
            
        else:
            form = FundraiserForm()
            print("erroruu")
            success = False
            error = 'Invalid form data. Please try again.'
    else:
        form = FundraiserForm()
    
    context = {'form': form, 'success': success, 'error': error}
    return render(request, 'user/newfunding.html', context)


def loadMyFundraisers(request):
    return render(request, 'loading/loadMyfundings.html')

def myFundraisers(request, id):
    fundraisers = [fundraiser for fundraiser in fundraisers_collection.find({'applicantId': id})]
    for fundraiser in fundraisers:
        fundraiser['id'] = str(fundraiser['_id'])
    return render(request, 'user/myfundraisers.html', {"fundraisers": fundraisers, "id": id})

def fundraiser(request, donarId, fundId):
    fund_id = bson.ObjectId(fundId)
    fundraiser = fundraisers_collection.find_one({'_id': fund_id})
    fundraiser['percentage'] = int((fundraiser['collectedAmount']/fundraiser['targetAmount']) * 100)

    donations = [donation for donation in donations_collection.find({"fundraiserId": fundId})]
    donations.reverse()

    success = False

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():

            objectId = bson.ObjectId(donarId)
            donar = users_collection.find_one({'_id': objectId})

            donarName = donar['username']
            donarEmail = donar['email']
            donationAmount = form.cleaned_data['amount']
            remark = form.cleaned_data['remarks']
            fundraiserId = fundId
            fundriserPurpose = fundraiser['purpose']

            donation = {
                "donarId": donarId, "donarName": donarName, "donarEmail": donarEmail, "donationAmount": donationAmount,
                "remark": remark, "fundraiserId": fundraiserId, "fundriserPurpose": fundriserPurpose
            }

            collectedAmount = int(fundraiser['collectedAmount']) + int(donationAmount)

            fundraisers_collection.update_one({'_id': fund_id}, {"$set": {"collectedAmount": collectedAmount}})

            result = donations_collection.insert_one(donation)

            success = True

    else:
        form = DonationForm()
        success = False

    return render(request, 'user/fundraiserdetails.html', {"fundraiser": fundraiser, "form": form, "donations": donations, "success": success, "donarId": donarId, "fundId": fundId})


def updateFundraiser(request, id):
    success = False
    error = ''
    if request.method == 'POST':
        form = FundraiserUpdateForm(request.POST)
        if form.is_valid():
            object_id = bson.ObjectId(id)

            applicantName = form.cleaned_data['applicantName']
            applicantEmail = form.cleaned_data['applicantEmail']
            applicantMobile = form.cleaned_data['applicantMobile']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            bannerImage = form.cleaned_data['bannerImage']
            purpose = form.cleaned_data['purpose']
            deadline = form.cleaned_data['deadline']
            targetAmount = form.cleaned_data['targetAmount']
            extraImage1 = form.cleaned_data['extraImage1']
            extraImage2 = form.cleaned_data['extraImage2']
            extraImage3 = form.cleaned_data['extraImage3']

            fundraisers_collection.update_one({"_id": object_id}, {"$set": {"applicantName": applicantName, "applicantEmail": applicantEmail, "applicantMobile": applicantMobile, "title": title,
                          "description": description, "bannerImage": bannerImage, "purpose": purpose, "deadline": deadline, "targetAmount": targetAmount, "collectedAmount": 0,
                          "extraImage1": extraImage1, "extraImage2": extraImage2,"extraImage3": extraImage3,}})
            success = True
  
            
        else:
            form = FundraiserForm()
            print("erroruu")
            success = False
            error = 'Invalid form data. Please try again.'
    else:
        object_id = bson.ObjectId(id)
        fundraiser = fundraisers_collection.find_one({'_id': object_id})
        if fundraiser is None:
            error = "Error in fetching Fundraiser!!"
            form = FundraiserUpdateForm()
        else:
            form = FundraiserUpdateForm(initial={
                            "applicantId": fundraiser['applicantId'], 
                            "applicantName": fundraiser['applicantName'], 
                            "applicantEmail": fundraiser['applicantEmail'], 
                            "applicantMobile": fundraiser['applicantMobile'], 
                            "title": fundraiser['title'],
                            "description": fundraiser['description'], 
                            "bannerImage": fundraiser['bannerImage'], 
                            "purpose": fundraiser['purpose'], 
                            "deadline": fundraiser['deadline'], 
                            "targetAmount": fundraiser['targetAmount'], 
                            "collectedAmount": fundraiser['collectedAmount'],
                            "extraImage1": fundraiser['extraImage1'], 
                            "extraImage2": fundraiser['extraImage2'],
                            "extraImage3": fundraiser['extraImage3'],
                        })
    
    context = {'form': form, 'success': success, 'error': error}
    return render(request, 'user/updatefunding.html', context)


def admin(request):
    fundraisers = [fundraiser for fundraiser in fundraisers_collection.find()]
    fundLen = len(fundraisers)

    users = [user for user in users_collection.find()]
    usersLen = len(users)

    donations = [donation for donation in donations_collection.find()]
    donationsLen = len(donations)

    totalDonation = 0

    for donation in donations:
        totalDonation += donation['donationAmount']

    return render(request, 'admin/admin.html', {"fundLen": fundLen, "usersLen": usersLen, "donationsLen": donationsLen, "totalDonation": totalDonation})

def allUsers(request):
    users = [user for user in users_collection.find()]
    for user in users:
        user['id'] = str(user['_id'])
    users.reverse()
    return render(request, 'admin/allusers.html', {"users": users})

def allFundraisers(request):
    fundraisers = [fundraiser for fundraiser in fundraisers_collection.find()]
    for fundraiser in fundraisers:
        fundraiser['id'] = str(fundraiser['_id'])
    fundraisers.reverse()
    return render(request, 'admin/allfundraisers.html', {"fundraisers": fundraisers})

def adminFundraiser(request, id):
    objectId = bson.ObjectId(id)
    fundraiser = fundraisers_collection.find_one({"_id": objectId})
    fundraiser['percentage'] = int((fundraiser['collectedAmount']/fundraiser['targetAmount']) * 100)
    donations = [donation for donation in donations_collection.find({"fundraiserId": id})]
    donations.reverse()

    return render(request, 'admin/adminFUndraiser.html', {"fundraiser": fundraiser, "donations": donations})

def allDonations(request):
    donations = [donation for donation in donations_collection.find()]
    donations.reverse()
    return render(request, 'admin/alldonations.html', {"donations": donations})