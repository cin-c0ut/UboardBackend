from django.db import models
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from backend.utils import hold_detection
import json
# from .gym import Gym

class Wall(models.Model):
    id = models.BigAutoField(primary_key=True)
    gym_id = models.ForeignKey('Gym', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    angle = models.FloatField()
    size = models.CharField(max_length=15)
    image = models.ImageField(upload_to='walls/')
    boxes = models.JSONField(default=list, blank=True) 
    confidences = models.JSONField(default=list, blank=True)
    classes = models.JSONField(default=list, blank=True)
    masks = models.JSONField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Call object detection to fill in information from image
        """
        if self.image:
            temp_image_path = default_storage.save(
                f'temp/{self.image.name}', ContentFile(self.image.read())
            )
            temp_image_full_path = default_storage.path(temp_image_path)

            try:
                detection_data = hold_detection(temp_image_full_path)
                self.boxes = json.dumps(detection_data['boxes'])
                self.confidences = json.dumps(detection_data['confidences'])
                self.classes = json.dumps(detection_data['classes'])
                self.masks = json.dumps(detection_data['masks'])
            finally:
                default_storage.delete(temp_image_path)

        super().save(*args, **kwargs) 