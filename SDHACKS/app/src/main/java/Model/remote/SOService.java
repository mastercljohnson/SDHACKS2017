package Model.remote;

import Model.model.examplesend;
import Model.model.exampleresponse
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

/**
 * Created by mastercljohnson on 10/21/2017.
 */

public interface SOService {
    @GET("/answers?order=desc&sort=activity&site=stackoverflow")
    Call<examplesend> getAnswers();

    @GET("/answers?order=desc&sort=activity&site=stackoverflow")
    Call<exampleresponse> getAnswers(@Query("tagged") String tags);
}
