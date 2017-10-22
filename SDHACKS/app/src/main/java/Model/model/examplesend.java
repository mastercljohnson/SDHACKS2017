package Model.model;

/**
 * Created by mastercljohnson on 10/21/2017.
 */




import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.List;

public class examplesend{

    @SerializedName("api_key")
    @Expose
    private String apiKey;
    @SerializedName("api_secret")
    @Expose
    private String apiSecret;
    @SerializedName("detection_flags")
    @Expose
    private List<String> detectionFlags = null;
    @SerializedName("image")
    @Expose
    private List<Object> image = null;
    @SerializedName("image_base64")
    @Expose
    private String imageBase64;
    @SerializedName("image_url")
    @Expose
    private String imageUrl;
    @SerializedName("original_filename")
    @Expose
    private String originalFilename;
    @SerializedName("set_person_id")
    @Expose
    private String setPersonId;

    public String getApiKey() {
        return apiKey;
    }

    public void setApiKey(String apiKey) {
        this.apiKey = apiKey;
    }

    public String getApiSecret() {
        return apiSecret;
    }

    public void setApiSecret(String apiSecret) {
        this.apiSecret = apiSecret;
    }

    public List<String> getDetectionFlags() {
        return detectionFlags;
    }

    public void setDetectionFlags(List<String> detectionFlags) {
        this.detectionFlags = detectionFlags;
    }

    public List<Object> getImage() {
        return image;
    }

    public void setImage(List<Object> image) {
        this.image = image;
    }

    public String getImageBase64() {
        return imageBase64;
    }

    public void setImageBase64(String imageBase64) {
        this.imageBase64 = imageBase64;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public String getOriginalFilename() {
        return originalFilename;
    }

    public void setOriginalFilename(String originalFilename) {
        this.originalFilename = originalFilename;
    }

    public String getSetPersonId() {
        return setPersonId;
    }

    public void setSetPersonId(String setPersonId) {
        this.setPersonId = setPersonId;
    }

}