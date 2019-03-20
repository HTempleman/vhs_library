from rest_framework import serializers
from vhs_library.models import Director, Distributor, Actor, Studio, Genre, Movie, BoxSet, Network


class DirectorSerializer(serializers.Serializer):
    class Meta:
        model = Director
        fields = ('first_name, last_name, middle_name, studio, comment')

class ActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = ('first_name, last_name, middle_name, comment')

class StudioSerializer(serializers.Serializer):
    class Meta:
        model = Studio
        fields = ('name, comment')

class DistributorSerializer(serializers.Serializer):
    class Meta:
        model = Distributor
        fields = ('name, comment')

class GenreSerializer(serializers.Serializer):
    class Meta:
        models = Genre
        fields = ('name, comment')

class BoxSetSerializer(serializers.Serializer):
    class Meta:
        models = BoxSet
        fields = ('name, comment')

class NetworkSerializer(serializers.Serializer):
    class Meta:
        models = Network
        fields = ('name, comment')


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many = True, required = False)
    actors = ActorSerializer(many = True, required = False)
    studios = StudioSerializer(many = True, required = False)
    distributors = DistributorSerializer(many = True, required = False)
    genres = GenreSerializer(many = True)


    class Meta: 
        model = Movie
        fields = ('director, actors, studio, genre, distributor, medium')

    def create(self, validated_data):
        try:
            director_data = validated_data.pop('directors')
        except:
            pass
        try:
            actor_data = validated_data.pop('actors')
        except:
            pass
        try:
            studio_data = validated_data.pop('studios')
        except:
            pass
        try:
            distributor_data = validated_data.pop('distributors')
        except:
            pass
        try:
            genre_data = validated_data.pop('genres')
        except:
            pass
        try:
            boxset_data = validated_data.pop('boxset')
        except:
            pass
        try:
            network_data = validated_data.pop('network')
        except:
            pass
        movie = Movie.objects.create(**validated_data)
        if director_data:
            for datum in director_data:
                try:
                    director = Director.objects.create(**director_data)
                    movie.directors.add(director)
                except:
                    pass
        if actor_data:
            for datum in actor_data:
                try:
                    actor = Actor.objects.create(**actor_data)
                    movie.actors.add(actor)
                except:
                    pass
        if studio_data:
            for datum in studio_data:
                try:
                    studio = Studio.objects.create(**studio_data)
                    movie.studios.add(studio)
                except:
                    pass
        if distributor_data:
            for datum in distributor_data:
                try:
                    distributor = Distributor.objects.create(**distributor_data)
                    movie.distributors.add(distributor)
                except:
                    pass
        if genre_data:
            for datum in genre_data:
                try:
                    genre = Genre.objects.create(**genre_data)
                    movie.genres.add(genre)
                except:
                    pass
        if boxset_data:
            for datum in boxset_data:
                try:
                    boxset = Boxset.objects.create(**boxset_data)
                    movie.boxset.add(boxset)
                except:
                    pass
        if network_data:
            for datum in network_data:
                try:
                    network = Network.objects.create(**network_data)
                    movie.network.update(network)
                except:
                    pass
        return movie
        