from django.db import models


# Class pour les categories
class Categories(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

# class pour les produits
class Produits(models.Model):
    name = models.CharField(max_length=100)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantite = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateField() 
    image = models.ImageField(null=True,blank=True,upload_to='media/')


    class Meta:
        ordering = ['-date_ajout']

    def status_quantite(self):

        # Si la quantite = 0 affiche rouge
        if self.quantite == 0:
            return 'red'
        
        # Sinon si la quantite est <= 10 affiche orange
        elif self.quantite <= 10:
            return 'orange'
        
        else:
            return 'green'
        
    def __str__(self):
        return self.name

# class pour les utilisateurs
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class pour la vente des produits
class Vente(models.Model):
    produit = models.ForeignKey(Produits,on_delete=models.CASCADE)
    sell_date = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.produit
    
    
# class pour la facture du client
class Facture_client(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_achat = models.DateTimeField(auto_now_add=False)
    total_amount = models.ForeignKey(Vente,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits,on_delete=models.CASCADE)

    def __str__(self):
        return f"Le recu de {self.customer.customer}"
    
