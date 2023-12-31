# compute_api_client.BatchJobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_job_batch_jobs_post**](BatchJobsApi.md#create_batch_job_batch_jobs_post) | **POST** /batch_jobs | Create batch job
[**enqueue_batch_job_batch_jobs_id_enqueue_patch**](BatchJobsApi.md#enqueue_batch_job_batch_jobs_id_enqueue_patch) | **PATCH** /batch_jobs/{id}/enqueue | Enqueue batch job for execution
[**finish_batch_job_batch_jobs_id_finish_patch**](BatchJobsApi.md#finish_batch_job_batch_jobs_id_finish_patch) | **PATCH** /batch_jobs/{id}/finish | Finish batch job
[**peek_batch_job_batch_jobs_peek_patch**](BatchJobsApi.md#peek_batch_job_batch_jobs_peek_patch) | **PATCH** /batch_jobs/peek | Peek batch job
[**pop_batch_job_batch_jobs_pop_patch**](BatchJobsApi.md#pop_batch_job_batch_jobs_pop_patch) | **PATCH** /batch_jobs/pop | Take batch job
[**read_batch_jobs_batch_jobs_get**](BatchJobsApi.md#read_batch_jobs_batch_jobs_get) | **GET** /batch_jobs | List batch jobs


# **create_batch_job_batch_jobs_post**
> BatchJob create_batch_job_batch_jobs_post(batch_job_in)

Create batch job

Create new batch job.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    batch_job_in = compute_api_client.BatchJobIn() # BatchJobIn | 

    try:
        # Create batch job
        api_response = api_instance.create_batch_job_batch_jobs_post(batch_job_in)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->create_batch_job_batch_jobs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_job_in** | [**BatchJobIn**](BatchJobIn.md)|  | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_batch_job_batch_jobs_id_enqueue_patch**
> BatchJob enqueue_batch_job_batch_jobs_id_enqueue_patch(id)

Enqueue batch job for execution

Enqueue batch job for execution.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    id = 56 # int | 

    try:
        # Enqueue batch job for execution
        api_response = api_instance.enqueue_batch_job_batch_jobs_id_enqueue_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->enqueue_batch_job_batch_jobs_id_enqueue_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_batch_job_batch_jobs_id_finish_patch**
> BatchJob finish_batch_job_batch_jobs_id_finish_patch(id)

Finish batch job

Finish batch job.

### Example

* Api Key Authentication (backend):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: backend
configuration.api_key['backend'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    id = 56 # int | 

    try:
        # Finish batch job
        api_response = api_instance.finish_batch_job_batch_jobs_id_finish_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->finish_batch_job_batch_jobs_id_finish_patch: %s\n" % e)
```

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: backend
configuration.api_key['backend'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    id = 56 # int | 

    try:
        # Finish batch job
        api_response = api_instance.finish_batch_job_batch_jobs_id_finish_patch(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->finish_batch_job_batch_jobs_id_finish_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[backend](../README.md#backend), [user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peek_batch_job_batch_jobs_peek_patch**
> BatchJob peek_batch_job_batch_jobs_peek_patch(request_body)

Peek batch job

Get batch job that can be taken up, excluding list of IDs.

### Example

* Api Key Authentication (backend):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: backend
configuration.api_key['backend'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    request_body = [56] # list[int] | 

    try:
        # Peek batch job
        api_response = api_instance.peek_batch_job_batch_jobs_peek_patch(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->peek_batch_job_batch_jobs_peek_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[int]**](int.md)|  | 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[backend](../README.md#backend)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pop_batch_job_batch_jobs_pop_patch**
> BatchJob pop_batch_job_batch_jobs_pop_patch()

Take batch job

Claim batch job by ID.

### Example

* Api Key Authentication (backend):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: backend
configuration.api_key['backend'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['backend'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    
    try:
        # Take batch job
        api_response = api_instance.pop_batch_job_batch_jobs_pop_patch()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->pop_batch_job_batch_jobs_pop_patch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[backend](../README.md#backend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_batch_jobs_batch_jobs_get**
> list[BatchJob] read_batch_jobs_batch_jobs_get()

List batch jobs

List batch jobs.

### Example

* Api Key Authentication (user):
```python
from __future__ import print_function
import time
import compute_api_client
from compute_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = compute_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Enter a context with an instance of the API client
with compute_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_api_client.BatchJobsApi(api_client)
    
    try:
        # List batch jobs
        api_response = api_instance.read_batch_jobs_batch_jobs_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BatchJobsApi->read_batch_jobs_batch_jobs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BatchJob]**](BatchJob.md)

### Authorization

[user](../README.md#user)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

