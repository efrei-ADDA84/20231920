# TP3

Pour deploy sur azure, le plus gros problème à été de setup cette partie:

```
          secure-environment-variables: |
            API_KEY=${{ secrets.API_KEY }}
          ports: 8081
```

de la partie `deploy`

sinon tout le reste s'est passé de manière fluide. l'api et le dockerfile marchaient déjà, tout ce qu'il y a eu à ajouter était le:

```
deploy:
    needs: build-and-push 
    runs-on: ubuntu-latest 
    
    steps: 
      - name: Login via Azure CLI
        uses: azure/login@v1
        with: 
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Deploy to Azure Container Instance
        uses: azure/aci-deploy@v1
        with: 
          resource-group: ${{ secrets.RESOURCE_GROUP }}
          dns-name-label: devops-20231920 
          image: ${{ secrets.REGISTRY_LOGIN_SERVER }}/20231920/weatherapp:latest 
          name: 20231920
          location: 'francecentral'
          registry-login-server: ${{ secrets.REGISTRY_LOGIN_SERVER }} 
          registry-username: ${{ secrets.REGISTRY_USERNAME }} 
          registry-password: ${{ secrets.REGISTRY_PASSWORD }}
```

